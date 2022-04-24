import unittest
from user import User
from credential import Credential

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
            
        def tearDown(self):
            '''
            tearDown method that cleans up after each test case is run
            '''

            User.user_list = []
            
        def test_find_credential(self):
            '''
            Test case to test if the User module is importing from Credential module
            '''

            # Save the new user
            self.new_user.save_user()

            test_user = User("Jane","doey")

            test_user.save_user()

            found_credential = User.find_credential("Yahoo")

            self.assertEqual( found_credential, False )
            
        def test_log_in(self):
            '''
            Test case to test if a user can log into their credentials
            '''

            # Save the new user
            self.new_user.save_user()

            test_user = User("Jane","doey")

            test_user.save_user()

            found_credential = User.log_in("Jane", "doey")

            self.assertEqual(found_credential,  Credential.credential_list)   
        
        def test_display_user(self):
            '''
            Test case to test if a user can see a list of all the users saved
            '''
            
            self.assertEqual(User.display_user(), User.user_list)

        def test_user_exist(self):
        
            '''
            Test to check if we can return a boolean if we can't find the user
            '''
            
            # Save the new user
            self.new_user.save_user()

            test_user = User("Jane","doey")

            test_user.save_user()
            
            # use contact exist method
            user_exists = User.user_exist("Jane")
            
            self.assertTrue(user_exists)


        # def test_delete_user(self):
        #     '''
        #     test_delete_user to test if you can remove user from user list 
        #     '''
        #     self.new_user.save_user()
        #     test_user = User('Test','67890') #new user
        #     test_user.save_user()
        #     self.new_user.delete_user() #deleting user
        #     self.assertEqual(len(User.user_list),1)    

if __name__ == '__main__':
    unittest.main()    