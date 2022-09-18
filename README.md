# AccountRegistration
Playing around with Flask

## Setting up Flask app
* export FLASK_APP=api
* export FLASK_DEBUG=1

## Creating Database in Python terminal
* The following will create a database table called User if it doesn't exist already
  * from api.models import User
  * from api import db, create_app
  * db.create_all(app=create_app())

## Checking Database
* In terminal: ``sqlite3 api/database``
* Run queries
  * Ex. ``select * from User`` shows whole database of users
