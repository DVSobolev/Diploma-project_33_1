from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.login_page import LoginPage
from utils.constant import VALID_PHONE_NUMBER, VALID_PASSWORD


def test_login_by_valid_phone_number(driver, base_url):
    '''
    Проверка авторизации по номеру телефона
    '''
    login_page = LoginPage(driver, base_url)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, login_page.PHONE_TAB)
    assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.ID, "//*[@id='login_input']"))  # исправил на локатор по тексту.
    # assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.NAME, "//h3[text()='Учетные данные']"))  # исправил на локатор по тексту. Но наверное логично проверять на наличие переданного логина, но как это сделать, там не пишется значение

# def test_login_by_valid_email(self, driver):
#     '''
#     Проверка авторизации по электронной почте
#     '''
#     login_page = LoginPage(self, driver)
#     login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, login_page.EMAIL_TAB)
#     assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.ID, "//*[@id='email_input']"))

#
# def test_login_by_valid_login(self, driver):
#     '''
#     Проверка авторизации по логину
#     '''
#     login_page = LoginPage(self, driver)
#     login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, login_page.LOGIN_TAB)
#     assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.ID, "//*[@id='login_input']"))
#
#
# def test_login_by_valid_personal_account(self, driver):
#     '''
#     Проверка авторизации по лицевому счёту. Т.к. данные для авторизации по лицевому счёту отсутствуют, то данный тест кейс не сработает. Необходимо в файле constant.py задать корректное значение для переменной VALID_LS
#     '''
#     login_page = LoginPage(self, driver)
#     login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, login_page.LS_TAB)
#     assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.ID, "//*[@id='login_input']"))



def test_product_slogan_after_auth(driver, base_url):
    '''
    Проверка наличия продуктового слогана ЛК "Ростелеком ID до авторизации
    '''
    login_page = LoginPage(driver, base_url)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, login_page.PHONE_TAB)
    assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.NAME,"//p[text()='Персональный помощник в цифровом мире Ростелекома']"))






    # def test_action_history(self):
    #     self.open()
    #     self.test_login_by_valid_phone_number()
    #     self.driver.find_element(By.XPATH, "//*[@id='app']/main/div[2]/div[4]/div/button").click()
    #     assert WebDriverWait(self.driver, 3).until(EC.element_to_be_clickbate(By.XPATH,"//*[@id='app']/main/div[2]/div/div[1]/div[2]/div[2]/span"))

















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
