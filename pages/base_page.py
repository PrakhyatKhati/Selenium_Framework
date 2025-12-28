from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# we have implement base class here
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10) # wait object with a 10 sec timeout


    def open(self,url:str):
        self.driver.get(url)

    def find(self,locator:tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click (self,locator:tuple):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def type(self,locator :tuple, text:str):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)
    # the above are all common method
    # also there might be some text that we have to extract.

    def text_of(self,locator :tuple) -> str:
        return self.find(locator).text.strip()

    def is_visible(self,locator:tuple)-> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False


