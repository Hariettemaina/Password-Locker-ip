#!/usr/bin/env python3.8
'''
This is the file that runs the application
Import User Class from User Module and Credential Class from Credential Module
'''
from user import User
from credential import Credential

    
def create_user(name, password):
     '''
    Function to create a user account
    Args:
        name : the name the user wants for the account
        password : the password the user want for the account
    '''

     new_user = User(name,password)

     return new_user

def save_users(user):
    '''
    Function to save a user account
    Args:
        user : the user account to be saved
    '''

    user.save_user()

def check_existing_users(name):
    '''
    Function that checks if a user account name already exists
    Args:
        name : the user account name
    '''

    return User.user_exist(name)

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)