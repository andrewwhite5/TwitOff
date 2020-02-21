# TwitOff
A web application for comparing Twitter users

'''sh

cd twitoff

FLASK_APP=app.py flask db init  #> Generates app/migrations dir

'''

## Migration

#> Run both when changing the schema

'''sh

FLASK_APP=app.py flask db migrate  #> Creates the db (with 'alembic_version' table)

FLASK_APP=app.py flask db upgrade  #> Creates the 'users' table

'''


## Run

'''sh

FLASK_APP=app.py flask run

'''
