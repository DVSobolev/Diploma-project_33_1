import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//*[@id='username']")
    USERPASSWORD = (By.XPATH, "//*[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='kc-login']")

    PHONE_TAB = (By.XPATH, "//*[@id='t-btn-tab-phone']")
    EMAIL_TAB = (By.XPATH, "// *[@id='t-btn-tab-mail']")
    LOGIN_TAB = (By.XPATH, "//*[@id='t-btn-tab-login']")
    LS_TAB = (By.XPATH, "//*[@id='t-btn-tab-ls']")

    def open_self(self):
        self.driver.get(f"{self.base_url}auth")
        return self

    def login(self, username: str, password: str, tab):
        time.sleep(5)
        self.driver.find_element(*tab).click()
        self.driver.find_element(self.USERNAME).send_keys(username)
        self.driver.find_element(self.USERPASSWORD).send_keys(password)
        self.driver.find_element(self.LOGIN_BUTTON).click()