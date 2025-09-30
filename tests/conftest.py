# # @pytest.fixture(scope='session')
# # def base_url():
# #     return 'https://b2c.passport.rt.ru/' # pytestconfig.getoptopn('--base-url')
# #
# # @pytest.fixture(scope='session')
# # def url_onlime_web():
# #     return 'https://my.rt.ru/'
#
#
# from selenium.webdriver.chrome.service import Service
# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope='session')
# def browser():
#     driver = webdriver.Chrome(executable_path="./chromedriver")
#     yield driver
#     driver.quit()
#
# @pytest.fixture(scope='session')
# def driver():
#     drv = webdriver.Chrome(service=Service())
#     yield drv
#     drv.quit()
#
# @pytest.fixture(scope='session')
# def base_url():
#     return 'https://b2c.passport.rt.ru/' # pytestconfig.getoptopn('--base-url')

from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def driver():
    drv = webdriver.Chrome(service=Service())
    yield drv
    drv.quit()

@pytest.fixture(scope='session')
def base_url():
    return 'https://b2c.passport.rt.ru/' # pytestconfig.getoptopn('--base-url')


@pytest.fixture(scope='session')
def url_start_web():
    return 'hhttps://start.rt.ru/'

@pytest.fixture(scope='session')
def url_smart_home_web():
    return 'https://lk.smarthome.rt.ru/'

@pytest.fixture(scope='session')
def url_key_web():
    return 'https://key.rt.ru/'

@pytest.fixture(scope='session')
def default_timeout():
    return 10