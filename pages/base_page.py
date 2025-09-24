from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url


    def setup(self):
        self.phone_number = settings.valid_phone_number
        self.user = settings.valid_email
        self.password = settings.valid_password
        self.login = settings.valid_login


    # def open(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("https://b2c.passport.rt.ru/")


    def close(self):
        self.driver.quit()