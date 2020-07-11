import unittest #Importing the unittest module
from user import User #Importing the user class
import Credential from credential 

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase class that helps in creating test cases
    """

def setUp(self):

    """
    set up method to run before each test case
    """

    #Create  user object
    self.new_user = User("Leroy","smith")

def test_init(self):

        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.first_name,"Leroy")
        self.assertEqual(self.new_user.middle_name,"Smith")
        
def tearDown(self):

        """
        tearDown method that does clean up after each test case has run.
        """

        User.users_list = []

def test_save_user(self):

        """
        test_save_user test case to test if the user object is saved into
         the users list
        """

        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.users_list), 1)

 def test_save_multiple_users(self):

        """
        test_save_multiple_users to check if we can save multiple users
        to our users_array
        """

        self.new_user.save_user_details()
        test_user = User("Test", "user", "0712345678", "test@user.com")  # new user
        test_user.save_user_details()
        self.assertEqual(len(User.users_list), 2)

 def test_display_user(self):

        '''
        Test case to test if a user can see a list of all the users saved
        '''
        
        self.assertEqual( User.display_user() , User.user_list )

 def test_user_exist(self):
        
        '''
        Test to check if we can return a boolean if we can't find the user
        '''

     # Save the new user
        self.new_user.save_user()

        test_user = User("Leroy","smith")

        test_user.save_user()
        
        # use contact exist method
        user_exists = User.user_exist("Jane")
        
        self.assertTrue(user_exists)

 def test_find_credential(self):

        '''
        Test case to test if the User module is importing from Credential module
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Leroy","smith")

        test_user.save_user()

        found_credential = User.find_credential()

        self.assertEqual( found_credential, False )
        
 

    







