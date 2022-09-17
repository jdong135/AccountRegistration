# AccountRegistration
Playing around with Flask

## Creating Database in Python terminal
* from api.models import User
* from api import db, create_app
* db.create_all(app=create_app())

## Checking Database
* In terminal: ``sqlite3 api/database``
* Run queries
  * Ex. ``select * from User`` shows whole database of users
