from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from utils.assertions import Assertions
from utils.constant import VALID_PHONE_NUMBER, VALID_PASSWORD, VALID_EMAIL, VALID_LOGIN, VALID_LS, INVALID_PHONE_NUMBER, INVALID_EMAIL,  INVALID_PASSWORD, INVALID_LOGIN, INVALID_LS
from utils.waits import Waiter

def test_check_logo_in_site_header(driver, base_url, default_timeout):
    '''
    Проверка наличия лого в шапке сайта                                                    ТЕСТ РАБОТАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    SITE_HEADRER = (By.CLASS_NAME, 'rt-logo')
    login_page.waiter.visible(SITE_HEADRER)
    login_page.assertion.element_visible(SITE_HEADRER)


def test_check_button_login_in_site_content(driver, base_url, default_timeout):
    '''
    Проверка наличия кнопки войти в контенте сайта                                           ТЕСТ РАБОТАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    LOGIN_BUTTON = (By.XPATH, '//*[@id="kc-login"]')
    login_page.waiter.visible(LOGIN_BUTTON)
    login_page.assertion.element_visible(LOGIN_BUTTON)


def test_check_support_number_in_site_footer(driver, base_url, default_timeout):
    '''
    Проверка наличия номера службы поддержки в подвале сайта                                 ТЕСТ РАБОТАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    SUPPORT_NUMBER = (By.XPATH, "//a[text()='8 800 100 0 800']")
    login_page.waiter.visible(SUPPORT_NUMBER)
    login_page.assertion.element_visible(SUPPORT_NUMBER)


def test_login_by_valid_phone_number(driver, base_url, default_timeout):
    '''
    Проверка авторизации по корректному номеру телефона                                      ТЕСТ РАБОТАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD,'phone')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)


def test_login_by_invalid_phone_number(driver, base_url, default_timeout):
    '''
    Проверка авторизации по некорректному номеру телефона                                  ТЕСТ РАБОТАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_PHONE_NUMBER, VALID_PASSWORD, 'phone')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)
    login_page.assertion.element_visible(FAIL_INFO)


def test_login_by_valid_email(self, driver):
    '''
    Проверка авторизации по корректной электронной почте                                ТЕСТ ПАДАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_EMAIL, VALID_PASSWORD, 'email')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)


def test_login_by_invalid_email(self, driver):
    '''
    Проверка авторизации по некорректной электронной почте                              ТЕСТ ПАДАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD, 'email')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)
    login_page.assertion.element_visible(FAIL_INFO)


def test_login_by_valid_login(self, driver):
    '''
    Проверка авторизации по корректному логину                                          ТЕСТ ПАДАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, 'login')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)

def test_login_by_invalid_login(self, driver):
    '''
    Проверка авторизации по некорректному логину                                         ТЕСТ ПАДАЕТ
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD, 'login')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)
    login_page.assertion.element_visible(FAIL_INFO)


def test_login_by_valid_personal_account(self, driver):
    '''
    Проверка авторизации по корректному лицевому счёту. Т.к. данные для авторизации по лицевому счёту отсутствуют, то данный тест кейс не сработает. Необходимо в файле constant.py задать корректное значение для переменной VALID_LS и изменить VALID_PASSWORD, соответственно
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_LS, VALID_PASSWORD,'login')
#     assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.ID, "//*[@id='login_input']"))
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)


def test_login_by_invalid_personal_account(self, driver):
    '''
    Проверка авторизации по некорректному лицевому счёту
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_LS, VALID_PASSWORD, 'ls')
#     assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.ID, "//*[@id='login_input']"))
    FAIL_INFO = (By.CLASS_NAME, 'error-message')
    login_page.waiter.visible(FAIL_INFO)


def test_product_slogan_after_auth(driver, base_url):
    '''
    Проверка наличия продуктового слогана ЛК "Ростелеком ID до авторизации
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    SITE_HEADRER = (By.CLASS_NAME, 'rt-logo')
    login_page.waiter.visible(SITE_HEADRER)
    login_page.assertion.element_visible(SITE_HEADRER)


    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD, 'phone')
    assert WebDriverWait(driver, 5).until(EC.element_to_be_clickbate(By.NAME,"//p[text()='Персональный помощник в цифровом мире Ростелекома']"))