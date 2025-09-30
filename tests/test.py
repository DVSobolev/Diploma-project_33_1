from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from utils import assertions
from utils.assertions import Assertions
from utils.constant import VALID_PHONE_NUMBER, VALID_PASSWORD, VALID_EMAIL, VALID_LOGIN, VALID_LS, INVALID_PHONE_NUMBER, INVALID_EMAIL,  INVALID_PASSWORD, INVALID_LOGIN, INVALID_LS
from utils.waits import Waiter


def test_check_auth_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия блока "Авторизация" на сайте
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    AUTH = (By.XPATH, '//h1[text()="Авторизация"]')
    login_page.waiter.visible(AUTH)
    login_page.assertion.element_visible(AUTH)


def test_check_tub_phone_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия переключателя "Телефон"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    login_page.waiter.visible(TAB_PHONE)
    login_page.assertion.element_visible(TAB_PHONE)


def test_check_tub_email_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия переключателя "Электронная почта"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    TAB_EMAIL = (By.ID, 't-btn-tab-mail')
    login_page.waiter.visible(TAB_EMAIL)
    login_page.assertion.element_visible(TAB_EMAIL)


def test_check_tub_login_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия переключателя "Логин"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    login_page.waiter.visible(TAB_LOGIN)
    login_page.assertion.element_visible(TAB_LOGIN)


def test_check_tub_personal_account_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия переключателя "Лицевой счёт"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    TAB_PERSONAL_ACCOUNT = (By.ID, 't-btn-tab-ls')
    login_page.waiter.visible(TAB_PERSONAL_ACCOUNT)
    login_page.assertion.element_visible(TAB_PERSONAL_ACCOUNT)


def test_check_button_login_in_site_content_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия кнопки "Войти"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    LOGIN_BUTTON = (By.ID, 'kc-login')
    login_page.waiter.visible(LOGIN_BUTTON)
    login_page.assertion.element_visible(LOGIN_BUTTON)


def test_check_button_forgot_password_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия нопки "Забыл пароль"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    FORGET_PASSWORD_BUTTON = (By.ID, 'forgot_password')
    login_page.waiter.visible(FORGET_PASSWORD_BUTTON)
    login_page.assertion.element_visible(FORGET_PASSWORD_BUTTON)


def test_check_button_registration_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия нопки "Регистрация"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    REGISTRATION_BUTTON = (By.ID, 'kc-register')
    login_page.waiter.visible(REGISTRATION_BUTTON)
    login_page.assertion.element_visible(REGISTRATION_BUTTON)

def test_check_button_hepl_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия нопки "Помощь"
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    HELP_BUTTON = (By.XPATH, '//a[text()="Помощь"]')
    login_page.waiter.visible(HELP_BUTTON)
    login_page.assertion.element_visible(HELP_BUTTON)


def test_check_support_number_in_site_footer_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия номера службы поддержки в подвале сайта
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    SUPPORT_NUMBER = (By.XPATH, "//a[text()='8 800 100 0 800']")
    login_page.waiter.visible(SUPPORT_NUMBER)
    login_page.assertion.element_visible(SUPPORT_NUMBER)


def test_check_user_agreement_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия пользовательского соглашения
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    USER_AGREEMENT = (By.ID, 'rt-auth-agreement-link')
    login_page.waiter.visible(USER_AGREEMENT)
    login_page.assertion.element_visible(USER_AGREEMENT)


def test_check_privacy_policy_in_site_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка наличия политики конфиденциальности
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    USER_AGREEMENT = (By.XPATH, "//span[text()=' Политикой конфиденциальности ']")
    login_page.waiter.visible(USER_AGREEMENT)
    login_page.assertion.element_visible(USER_AGREEMENT)


def test_login_by_valid_phone_number_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по корректному номеру телефона
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD,'phone')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)


def test_login_by_invalid_phone_number_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по некорректному номеру телефона
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_PHONE_NUMBER, VALID_PASSWORD, 'phone')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)
    login_page.assertion.element_visible(FAIL_INFO)


def test_login_by_valid_email_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по корректной электронной почте
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_EMAIL, VALID_PASSWORD, 'email')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)


def test_login_by_invalid_email_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по некорректной электронной почте
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD, 'email')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)
    login_page.assertion.element_visible(FAIL_INFO)


def test_login_by_valid_login_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по корректному логину
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_LOGIN, VALID_PASSWORD, 'login')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)

def test_login_by_invalid_login_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по некорректному логину
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD, 'login')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)
    login_page.assertion.element_visible(FAIL_INFO)


def test_login_by_valid_personal_account_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по корректному лицевому счёту.                                ТЕСТ ЗАРАБОТАЕТ, если: т.к. данные для авторизации по лицевому счёту отсутствуют, то данный тест кейс не сработает.
    Необходимо в файле constant.py задать корректное значение для переменной VALID_LS и изменить VALID_PASSWORD при необходимости, соответственно
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(VALID_LS, VALID_PASSWORD,'ls')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)


def test_login_by_invalid_personal_account_lk_rt(driver, base_url, default_timeout):
    '''
    Проверка авторизации по некорректному лицевому счёту
    '''
    login_page = LoginPage(driver, base_url, default_timeout)
    login_page.open_self()
    login_page.login(INVALID_LS, VALID_PASSWORD, 'ls')
    FAIL_INFO = (By.CLASS_NAME, 'card-error__message')
    login_page.waiter.visible(FAIL_INFO)

# __________________________________

def test_login_by_valid_phone_number_onlime_web(driver, url_onlime_web, default_timeout):
    '''
    Проверка авторизации по корректному номеру телефона                                      ТЕСТ НЕ CРАБАТЫВАЕТ (не осуществляется переход на страницу авторизации с 3 способами авторизации)
    '''
    login_page = LoginPage(driver, url_onlime_web, default_timeout)
    login_page.open_self()
    login_page.login(VALID_PHONE_NUMBER, VALID_PASSWORD,'phone')
    USER_INFO = (By.CLASS_NAME, 'user-info')
    login_page.waiter.visible(USER_INFO)
    login_page.assertion.element_visible(USER_INFO)