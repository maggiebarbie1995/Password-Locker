import random
from user import User
from credential import Credential

# Create a user

def create_user(fname, mname,password):

    """
    Function to create a new user
    """

    new_user = User(fname, mname,password)
    return new_user

    # Save user

def save_user(user):

    """
    Function to save contact
    """

    user.save_user_details()

    # Delete user

def del_user(user):

    """
    Fuction to delete a contact
    """

    user.delete_user()

    # Finding user

def display_user():

    """
    Function that finds and returns saved users
    """

    return User.display_users()

    # Display credentials

def display_cred():

    """
    Function that returns saved user credentials
    """

    return Credential.display_credential()

def create_credential(fname,mname,password):

    """
    Function to create new user credentials
    """

    new_credential = Credential(fname,mname,password)

    return new_credential

def verify_user(fname,mname,password):

    checking_user = Credential.check_user(fname,mname,password)

    return checking_user

def save_cred(credential):

    """
    Function to save user credentials
    """

    credential.save_credential()

def del_cred(credential):

    """
    Function to delete all users credentials
    """
    
    credential.delete_credential()









    














