# python/users/views.py


#################################################
#### imports                                #####
#################################################

from functools import wraps
from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, Blueprint
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from .forms import RegistrationForm, LoginForm
from project import db
from project.models import User


#################################################
##### config                               #####
#################################################
users_blueprint = Blueprint('users', __name__)

#################################################
#### helper functions
#################################################
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


#################################################
# route handlers
#################################################
@users_blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
    #return render_template('_base.html', form=form, error=error)

@users_blueprint.route('/top/', methods=['GET', 'POST'])
def top():
    return render_template('top.html')
    #return render_template('_base.html', form=form, error=error)


#@app.route('/', methods=['GET', 'POST'])
@users_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                session['role'] = user.role
                flash('Welcome!')
                #return redirect(url_for('tasks.tasks'))
                return redirect(url_for('users.welcome'))
            

            else:
                error = 'Invalid username or password.'
        else:
            error = 'Both fields are required.'
            #return redirect(url_for('users.login'))
    
    return render_template('login.html', form=form, error=error)
        

@users_blueprint.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    error = None
    form = LoginForm(request.form)
    return render_template('welcome.html')


#@app.route('/logout/')
@users_blueprint.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('role', None)
    flash('Goodbye!')
    return redirect(url_for('users.login'))



#################################################
##### Registration                          #####
#################################################
@users_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data,
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering, Please login.')
                return redirect(url_for('users.login'))     
            except IntegrityError:
                error = 'That username and/or email already exist.'
                return render_template('register.html', form=form, error=error)
    return render_template('register.html', form=form, error=error)
