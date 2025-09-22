from selenium import webdriver

# from api import TestLoginRostelecom
import settings


class TestLoginRostelecom:
    def setup(self):
        self.phone_number = settings.valid_phone_number
        self.user = settings.valid_email
        self.password = settings.valid_password
        self.login = settings.valid_login


    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru/")


    def close(self):
        self.driver.quit()


    def test_login_by_valid_phone_number(self):
        self.driver.find_element(By.XPATH, "//*[@id='t-btn-tab-phone']").click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        assert WebDriverWait(self.driver, 5).until(EC.element_to_be_clickbate(By.XPATH, "//*[@id='app']/main/div[2]/div[2]/div/h3"))


    def test_login_by_valid_email(self):
        self.driver.find_element(By.XPATH, "// *[@id='t-btn-tab-mail']").click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        assert WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(By.XPATH, "//*[@id='app']/main/div[2]/div[2]/div/h3"))


    def test_login_by_valid_login(self):
        self.driver.find_element(By.XPATH, "//*[@id='t-btn-tab-login']").click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        assert WebDriverWait(self.driver, 5).until(EC.element_to_be_clickbate(By.XPATH, "//*[@id='app']/main/div[2]/div[2]/div/h3"))


    def test_login_by_valid_personal_account(self):
        self.driver.find_element(By.XPATH, "//*[@id='t-btn-tab-ls']").click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        assert WebDriverWait(self.driver, 3).until(EC.element_to_be_clickbate(By.XPATH, "//*[@id='app']/main/div[2]/div[2]/div/h3"))


    def test_action_history(self):
        self.open()
        self.test_login_by_valid_phone_number()
        self.driver.find_element(By.XPATH, "//*[@id='app']/main/div[2]/div[4]/div/button").click()
        assert WebDriverWait(self.driver, 3).until(EC.element_to_be_clickbate(By.XPATH,"//*[@id='app']/main/div[2]/div/div[1]/div[2]/div[2]/span"))

















# pf = Authorization()
#
# def test_get_api_key_for_valid_user(username=valid_email, password=valid_password):
#     status, result = pf.get_api_key(username, password)
#     assert status == 200
#     assert 'key' in result
#     print(result)




















# import requests
# import json


# class Authorization:
#     def __init__(self):
#         self.base_url = "https://b2c.passport.rt.ru/"
#
#
#     def get_api_key(self, username, password):
#         headers = {
#             'username': username,
#             'password': password
#         }
#         res = requests.post(self.base_url + 'api/fl/idw-rt-lk', headers=headers)
#         status = res.status_code
#         result = ''
#         try:
#             result = res.json()
#         except json.JSONDecodeError:
#             result = res.text
#         print(result)
#         return status, result






# res = requests('https://b2c.passport.rt.ru/', heeaders={'acccept': 'application/json'})
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(type(res.json()))
