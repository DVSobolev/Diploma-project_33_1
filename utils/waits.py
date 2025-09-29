from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




DEFAULT_POLL = 0.2
IGNORED = (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException)

class Waiter:
    def __init__(self, driver, timeout: int, poll: float = DEFAULT_POLL):
        self.driver = driver
        self.timeout = timeout
        self.poll = poll

    def until(self, condition):
        return WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll, ignored_exceptions=IGNORED).until(condition)

    def visible(self, locator):
        return self.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.until(EC.element_to_be_clickable(locator))

    def present(self, locator):
        return self.until(EC.presence_of_element_located(locator))

    def gone(self, locator):
        return self.until(EC.invisibility_of_element_located(locator))

    def text_to_be(self, locator, text):
        return self.until(EC.text_to_be_present_in_element(locator, text))
