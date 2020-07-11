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







