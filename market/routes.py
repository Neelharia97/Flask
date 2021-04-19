from market import app
from flask import render_template, redirect,url_for,flash
from market.models import Item, User
from market import db

#Importing Register Form to route the user to the form if someone clicks Register
from market.forms import RegisterForm

#Route Url - Route function gives you the the web page at base_url/---
@app.route('/')
@app.route('/base')
def login_world():
    return render_template('base.html')

#This route will take you to base_url/about
@app.route('/about')
def login_about():
    return "This is about page"

#
@app.route('/home')
def home_page():
    #Render templates helps in routing to different templates in different locations
    return render_template('home.html')

@app.route('/market')
def market_page():
    # item_names can be used to send information to the route
    items = Item.query.all()
    return render_template('market.html', items = items)

#Routing to Register.html to create new user
@app.route('/register', methods = ['POST','GET'])
def register_page():
    #importing all user fields from forms.py
    form = RegisterForm()
    #After user enters the details for a new user creation
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email_address = form.email_address.data,
                              password_hash = form.password1.data)
        #Adding to database and then committing
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_message in form.errors.values():
            flash(f'There was an error with creating a User: {err_message}', category='danger')
    # 'forms' used in register.html to access data from forms.py under RegisterForm class
    return render_template('register.html', forms = form)