from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from Project.Ebay import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/find-deals")
def dealsPage():
    items = Item.query.all()
    return render_template("deals.html", items=items)

# @app.route("/about/<username>")
# def about_page(username):
#    return f"<h1>About Page of {username}</h1>
