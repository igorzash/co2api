# co2ding api

## Deploy

### Prod

#### Docker + Heroku

```sh
heroku container:push web -a APP_NAME # build and push
heroku container:release web -a APP_NAME
```

### Local

```sh
python init_db.py # init database from csv dataset
uvicorn app:app
```