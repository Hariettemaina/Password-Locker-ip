import unittest
from user import User

class TestUser(unittest.TestCase):
    
        '''
        Test class that defines test cases for the User class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
        '''

        def setUp(self):
            '''
            Set up method to run before each test cases. 
            '''

            #Create a user object
            self.new_user = User('Hariettemaina','12345')

        def test_init(self):
            '''
            Test case to check if the object is initialized properly
            '''

            self.assertEqual(self.new_user.user_name, 'Hariettemaina')
            self.assertEqual(self.new_user.user_password, '12345')

        def test_save_user(self):
            '''
            test_save_user test case to test if the user object is saved to the user list
            '''
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

        def test_delete_user(self):
            '''
            test_delete_user to test if you can remove user from user list 
            '''
            self.new_user.save_user()
            test_user = User('Test','67890') #new user
            test_user.save_user()
            self.new_user.delete_user() #deleting user
            self.assertEqual(len(User.user_list),1)    

if __name__ == '__main__':
    unittest.main()    