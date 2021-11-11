from Scrape import app
from flask import render_template, redirect, url_for,flash
from Scrape.forms import RegisterForm
from Scrape.models import Item,User
from Scrape import db

@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/find-deals")
def dealsPage():
    items = Item.query.all()
    return render_template("deals.html", items=items)

@app.route("/register",methods=["GET","POST"])
def registerPage():
    form = RegisterForm()
    if form.validate_on_submit():
        userToCreate = User(username=form.username.data,email=form.email.data,
                        pwdHash=form.pwd1.data)
        db.session.add(userToCreate)
        db.session.commit()
        return redirect(url_for('dealsPage'))
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"Registration Error: {' '.join(error_msg)}",category='danger')



    return render_template('register.html',form=form)
