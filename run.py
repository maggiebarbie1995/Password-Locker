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





    














