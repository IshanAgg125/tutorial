from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
# cross origin request, send request to backend from a different URL
# Protected so the server does not get hit from a different URL

app = Flask(__name__) # initializing the flask application
CORS(app) # cross origin request to our server

# initializing database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# specifying the location of the local sql lite database that we will be storing in the database

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# not keeping track of modifications

# instance of the database

db = SQLAlchemy(app) # create a DB instance of what we have defined

# this is an ORM, object relation management






