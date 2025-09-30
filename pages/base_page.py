from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest

from tests.conftest import default_timeout
from utils.assertions import Assertions
from utils.waits import Waiter


class BasePage:
    def __init__(self, driver, base_url, default_timeout):
        self.driver = driver
        self.base_url = base_url
        self.waiter = Waiter(driver, timeout=default_timeout)
        self.assertion = Assertions(self.waiter)


    def open(self, path: str = ""):
        url = f"{self.base_url}/{path}"
        self.driver.get(url)
        return self


    def close(self):
        self.driver.quit()

