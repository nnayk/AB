from flask_login.utils import logout_user
from Scrape import app
from flask import render_template, redirect, url_for, flash,request
from Scrape.forms import RegisterForm,LoginForm,FilterForm
from Scrape.models import Item, User
from Scrape import db
from Scrape.General import General
from flask_login import login_user,logout_user,login_required



@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/find-deals",methods=["GET", "POST"])
@login_required
def dealsPage():
    products_list={}
    titles=[]
    items=''
    sort=""
    jiggle = FilterForm()
    if request.method=="POST":
        productEntered = request.form.get("search","")
        if productEntered=='':
            return render_template("deals.html",jiggle=jiggle,items='',titles='',sort=sort)
        sort_by = jiggle.filterMode.data
        #print(f"jigglypuff={sort}")
        storeObj = General("Ebay")
        titles = ["Name","Image","Price","Condition","Shipping","Options"]
        products_list = storeObj.startScrape(productEntered,sort_by)
        items = products_list
    return render_template('deals.html', jiggle=jiggle,items=items,titles=titles)


@app.route("/register", methods=["GET", "POST"])
def registerPage():
    form = RegisterForm()
    if form.validate_on_submit():
        userToCreate = User(username=form.username.data, email=form.email.data,
                            password=form.pwd1.data)
        db.session.add(userToCreate)
        db.session.commit()
        login_user(userToCreate)
        flash(f"Welcome, {userToCreate.username}",category='success')
        return redirect(url_for('dealsPage'))
    if form.errors != {}:
        for error_msg in form.errors.values():
            if ' '.join(error_msg)=='Field must be equal to pwd1.':
                error_msg=['Passwords', 'must', 'match.']

            flash(
                f"Registration Error: {' '.join(error_msg)} Try again.", category='danger')

    return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        enteredUser = User.query.filter_by(username=form.usernameOrEmail.data).first()
        if enteredUser and enteredUser.checkPassword(enteredPwd=form.pwd.data):
            login_user(enteredUser)
            flash(f"Welcome back, {enteredUser.username}",category='success')
            return redirect(url_for('dealsPage'))
        else:
            flash(f"Invalid username or password. Try again or create an account.",category='danger')
   

    return render_template('login.html', form=form)

@app.route("/logout")
def logoutPage():
    logout_user()
    flash("Successfully logged out. We hope to see you again.",category="info")
    return redirect(url_for("homePage"))
