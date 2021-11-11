from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from Project.Ebay import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '194e8b78e4d7cfd736b218d4'
db = SQLAlchemy(app)

from Scrape import routes