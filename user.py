'''
Import Credential from credential module to access an account's credentials
'''
from credential import Credential

class User:
    '''
     class that generates new instances of user account
    '''
    #Empty list of users
    user_list = []
    
    
    def __init__(self, user_name, password):
        '''
        __init__ method to define the properties of a User object
        Args:
            user_name : name of a user
            user_password : password for a user
        '''
        self.user_name = user_name
        self.user_password = password
             
        
    def save_user(self):
        '''
        Method that saves a user to user list
        '''
        User.user_list.append(self)
    
    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self) 
        
    @classmethod
    def display_users(cls):
        '''
        method that retuns info from the userlist
        '''        
        return cls.user_list
    
    @classmethod
    def find_credential(cls, name):
        '''
        Method that checks if Credentials is imported correctly
        Args:
            name : name of the credential
        Returns:
            Boolean : True / False if the credential exists or does not exist
        '''

        # Search for the user in the user list
        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
         '''
        Method that allows a user to log into their credential
        Args:
            name : name of the user
            password : password for the user
        Returns:
            Credential list for the user that matches the name and password
            False: if the name or password is incorrect
        '''

        # Search for the user in the user list
         for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credential.credential_list  
         return False
     
    @classmethod
    def user_exist(cls, name):
        '''
        Method that checks if a user exists in the user list
        
        Args:
            name: name of the user to search
            
        Returns:
            Boolean: true/false depending if the user exists
            
        '''
        
        for user in cls.user_list:
            if user.user_name == name:
                return True
            
        return False

    