from sanic import Sanic
from sanic.response import json

from metapensiero.pj.api import translates

DEFAULT_API_KEY = 'pyecharts-0-5-0-rocks'


class Python2Javascript:
    @staticmethod
    def translate(source_lines):
        javascript, _ = translates(source_lines)
        return ''.join(javascript)


app = Sanic()


@app.route('/translate', methods=['POST'])
async def translate(request):
    incoming_header = request.headers.get('authorization')
    if incoming_header == DEFAULT_API_KEY:
        javascript = Python2Javascript.translate(request.json['source'])
        return json({'response': javascript})
    else:
        return json(
            {'message': 'Invalid API Key'},
            headers={'X-Served-By': 'sanic'},
            status=403
            )


@app.route('/', methods=['GET'])
async def home(request):
    return json({
        "message": "An api server to convert python 3 code to javascript"}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
