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
    Function to delete a contact
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

def main():
    print("Hello! Welcome to your Password Locker.Choose the right way from the above methods")  

while True:
        print("\n a - create a new user account with a Personal password\n b - create a new user account with an auto-generated password\n c - Display all user accounts \n d - Login  to an existing Account\n ex -exit the contact list \n")    
     
        short_code = input().lower()

        if short_code == 'a':
                            print("New User")
                            print("-"*10)
                            print("Hi! Which site do you wish to create an account?")
                            site = input()
                            print(f"Welcome {site}?")

                            print ("First name ....")
                            f_name = input()

                            print("Middle name ...")
                            m_name = input()

                            print("Enter Password ...")
                            password = input()
                           
                            save_user(create_user(f_name,m_name)) # create and save new contact.                            
                            print ('\n')
                            print(f"New {site} account by {f_name} {m_name} successfully created")
                            print(f" username is {user_name} and the password is {password}") 
                            print ('\n')

        elif short_code == 'b':
                        print("New User")
                        print("-"*10)
                        print("Hi! Which site do you wish to create an account?")
                        site = input()
                        print(f"Welcome {site}?")

                        print ("First name ....")
                        f_name = input()

                        print("Middle name ...")
                        m_name = input()

                        print("Enter Password ...")
                        password = input()


                        save_user(create_user(f_name,m_name)) # create and save new contact.
                        save_cred(create_credential(user_name, pword, e_address))  # create and save a credential listing for the above user                            
                        print ('\n')
                        print(f"New {site} account by {f_name} {m_name} successfully created")
                        print(f" username is {user_name} and the password is {password}") 
                        print ('\n')

        elif short_code == 'c':

            if display_user():
                                print("")
                                print('\n')

            for user in display_user():
                                    print(f"{user.first_name}) {user.middle_name} has an account{site}")
                                    print('\n')

            else:
                                    print('\n')
                                    print("you don't have any existing account")
                                    print('\n')

        elif short_code == "d":
                                   print("-"*60) 
                                   print(' ')
                                   print('To login, enter your account details:')
                                   user_name = input('Enter your first name - ').strip()
                                   pword = str(input('Enter your password - '))
                                   user_exists = verify_user(user_name,password)

        if user_exists == user_name:
                                   print("")
                                   print(f'Welcome {user_name}.Choose an option to continue.')                
                                   print(' ')
while True:
                                   print("-"*60)

            for user in display_user():             
                                   print(f"{user.first_name} {user.middle_name} has an account for {site}")
                    
            else: 
                                   print('Wrong details entered please try again or create a new account.') 

        elif short_code == "ex":
                                   print("Bye .......")
                                   break

            else:
                                  print(" Please use the short codes")

        if __name__ == '__main__':
            main()







    














