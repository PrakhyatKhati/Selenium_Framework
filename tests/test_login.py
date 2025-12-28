# we need to import from pages
from pages.login_page import LoginPage
import time

def test_login(driver,base_url,credentials):
    login_page = LoginPage(driver)
    login_page.load(base_url)
    login_page.login(credentials["username"],credentials["password"])
    time.sleep(5)
