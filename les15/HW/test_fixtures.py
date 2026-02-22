

"""
Сделайте разные фикстуры для каждого теста,
 которые выставят размеры окна браузера
"""


import pytest
from selene import browser, have

@pytest.fixture(autouse=True)
def browser_managment():
    browser.config.base_url = 'https://github.com/'
    yield
    browser.quit()

@pytest.fixture
def browser_desktop():
    browser.open('')
    browser.driver.set_window_size(1920, 1080)
    return browser

@pytest.fixture
def browser_mobile():
    browser.open('')
    browser.driver.set_window_size(375, 812)
    return browser


def test_github_desktop(browser_desktop):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))

def test_github_mobile(browser_mobile):
    browser.element("//a[contains(@class,'HeaderMenu-link') and contains(., 'Sign in')]").click()
    browser.should(have.url('https://github.com/login'))