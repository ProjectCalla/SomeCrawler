__author__ = 'j'
class LoginException(Exception):
    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super(LoginException, self).__init__("Coulnt log in. Check your username and password.")

        # Now for your custom code...
        self.errors = "Login Error"