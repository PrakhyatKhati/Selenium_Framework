from selenium.webdriver.common.by import By
from .base_page import BasePage

# we have to inheriate the base page so that we can reuse them

class LoginPage(BasePage):
    UserName = (By.ID, "user-name")
    Password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    # load the application
    def load(self,base_url:str):
        self.open(base_url)

    # now try to login to the page
    def login (self, username:str,password:str):
        self.type(self.UserName,username)
        self.type(self.Password,password)
        self.click(self.login_btn)


