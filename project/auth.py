from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/trainer_login')
def trainer_login():
    return 'Trainer Login'
@auth.route('/client_login')
def client_login():
    return 'Client Login'

@auth.route('/trainer_signup')
def trainer_signup():
    return 'Trainer Signup'

@auth.route('/client_signup')
def client_signup():
    return 'Client Signup'

@auth.route('/logout')
def logout():
    return 'Logout'
