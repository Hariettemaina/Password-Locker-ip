class Credential:
    '''
    Class that generates instances of a users credentials
    '''

    # Empty list of credentials
    credential_list = []

    def __init__(self, user_password, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        Args:
            user_password : password of the user
            credential_name : name of an account
            credential_password : password for the account
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    