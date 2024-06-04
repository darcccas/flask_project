import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



basedir = os.getcwd()

directory = 'database'
if not os.path.exists(directory):
    os.mkdir(directory)


app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "4654f5dfadsrfasdr54e6rae"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, directory, "data.sqlite"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


from page import routes



