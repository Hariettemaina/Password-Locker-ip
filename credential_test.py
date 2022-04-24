import unittest
from  credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
 
    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create credential object
        self.new_credential = Credential("doe","Yahoo","yahoo17")
        
    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list = []
        
    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''
        self.assertEqual(self.new_credential.user_password, "doe")
        self.assertEqual(self.new_credential.credential_name, "Yahoo")
        self.assertEqual(self.new_credential.credential_password, "yahoo17")
