# pyecharts-javascripthon-api-service

Bring pyecharts-javascripthon to python 2.7 and 3.4 users.

If you use python 3.5 and python 3.6, you do NOT need this service. Thanks for your reading.


## Host the api server by yourself

### Heroku

Please follow the heroku [get started guide](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

0. You need to sign up a free account.

1. Prepare the app

``` shell
git clone https://github.com/pyecharts/pyecharts-javascripthon-api-service.git
cd pyecharts-javascripthon-api-service
```

2. Deploy the app

``` shell
$ heroku create
$ git push heroku master
```

3. Use it

``` shell
export SCRIPTHON_API_ENDPOINT=https://your_app.heroku.com/translate
```

## Requirements

Python 3.6


## License

MIT
