# hangman-server

Hangman REST API written in python using flask

## Getting started

Make sure you're using python 3.8

Setup virtual env and Install requirements

```shell
make install
```

Run the tests

```shell
make test
```

Start server

```shell
make start
```

Hit the API

```
POST http://localhost:5000/api/hangman
GET http://localhost:5000/api/hangman/{game_id}
POST http://localhost:5000/api/hangman/{game_id}/guess
```
