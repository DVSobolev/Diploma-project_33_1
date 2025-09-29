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


    def open_onlime_web(self):
        self.driver.get(f"{self.url_onlime_web}auth")
        return self


    def login(self, username: str, password: str, tab_type:str):
        time.sleep(5)
        # self.driver.find_element(*tab).click()
        if tab_type == "phone":
            self.driver.find_element(By.ID, "t-btn-tab-phone").click()
        if tab_type == "mail":
            self.driver.find_element(By.ID, "t-btn-tab-mail").click()
        if tab_type == "login":
            self.driver.find_element(By.ID, "t-btn-tab-login").click()
        if tab_type == "ls":
            self.driver.find_element(By.ID, "t-btn-tab-ls").click()

        # self.driver.find_element(self.USERNAME).send_keys(username)
        self.waiter.visible(self.USERNAME).send_keys(username)
        self.waiter.visible(self.USERPASSWORD).send_keys(password)
        self.waiter.visible(self.LOGIN_BUTTON).click()