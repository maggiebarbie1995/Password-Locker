class User:

  """
  Import Credential from credential module to access account credential

  Class that generates new instances of user
  """

  user_list = []

def __init__(self,first_name,middle_name,password):
      self.first_name = first_name
      self.middle_name = middle_name
      self.password = password

def save_user(self):

      """
      save_user method saves a new user objects to the user_list
      """

      User.user_list.append(self)

@classmethod
def find_credentials(cls,name):

      """
      Method that checks if Credentials is imported correctly

      Args:
      name:name of the credential

      Returns:
      Boolean:True/False if the credential exists or does not exist
      """

        # search for the user in the user list
  for credential in User.user_list:
    if credential.credential_name == name:
        return True

        return False

@classmethod
def log_in(cls, name,password):

      """
      Method that allows a user to log into their credential

      Args:
        name: name of the user
        password:password for the user

      Returns:
        Credential list for the user that matches the name and password
        False: if the name or password is incorrect
      """

  for User in cls.user_list:
    if User.user_name == name and User.user_password == password:
          return User.user_list

          return False

@classmethod
def display_user(cls):

      """
      Method that returns the user list
      """

      return cls.user_list

@classmethod
def user_exist(cls,name):

      """
      Method that checks if a user exists in the user list

      Args:
         name:name of the user to search

      Returns:
         Boolean:true/false depending if the user exists

      """

      for user in cls.user_list:
        if User.user_name == name:
          return True

          return False


   









