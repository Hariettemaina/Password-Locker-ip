import unittest
from user import User


class Testuser(unittest.TestCase):
    
     '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
def setUp(self):
    '''
    Set up method to run before each test casees. 
    '''
    
    #Create a user object
    self.new_user = User('Jolly2022' '12345')
    
def test__init__(self):
    '''
    Test case to check if the object is initialized properly
    '''
    
    self.asserEqual( self.new_user.user_name, 'Jolly')
    self.assertEqual( self.new_user.user_password, '12345')
    