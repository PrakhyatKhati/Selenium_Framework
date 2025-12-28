# conftest.py is a special pytest configuratioon file that defines shared fictures hoks and plugins for test files
# so that the testing will be consistant and predictable environmen or set of resoursces that tests can use.
import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# we need to use decorator to identify test fixture.

# fixture are constant functions that setup the resourse before we start with anything
load_dotenv()
@pytest.fixture()
def driver():

    opts = Options()
    opts.add_experimental_option("prefs",{
        "credentials_enable_service": False,
        "profile.password_manager_enabled":False,
        "profile.password_manager_leak_detection":False

    })
    # this option disables the chrome password manager, preveting save password etc.popup that interfere with cselenium automation tests.

    driver = webdriver.Chrome(options= opts)
    driver.maximize_window()

    # this is here to teardown  the browser.
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
            }
