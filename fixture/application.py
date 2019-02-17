from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(2)
        self.exceptions = exceptions
        self.waits = WebDriverWait

    def destroy(self):
        pass

