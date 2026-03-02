from selene import browser, have
from allure_commons._allure import step
import requests

LOGIN = 'PDV63@mail.ru'
PASSWORD = 'Passw0rd'

url = 'https://demowebshop.tricentis.com'
API_URL = 'https://demowebshop.tricentis.com/login'


def test_login():

    with step('Open login page'):
        browser.open('https://demowebshop.tricentis.com/login')

    with step('Fill login form'):
        browser.element('#Email').send_keys(LOGIN)
        browser.element('#Password').send_keys(PASSWORD).press_enter()

    with step ('Varify successful authorization'):
        browser.element('.account').should(have.text(LOGIN))


def test_login_api():

    # with step('Open login page'):
    #     browser.open('https://demowebshop.tricentis.com/login')
    #
    # with step('Fill login form'):
    #     browser.element('#Email').send_keys(LOGIN)
    #     browser.element('#Password').send_keys(PASSWORD).press_enter()

    result = requests.post(
        url=API_URL,
        data={'Email':LOGIN,
             'Password':PASSWORD}
    )
    print(result.text)
    print(result.cookies)
'14:28'
    # with step ('Varify successful authorization'):
    #     browser.element('.account').should(have.text(LOGIN))