from selene import browser, have
from allure_commons._allure import step
import requests
import allure
from allure_commons.types import AttachmentType

LOGIN = 'PDV63@mail.ru'
PASSWORD = 'Passw0rd'

url = 'https://demowebshop.tricentis.com'
API_URL = 'https://demowebshop.tricentis.com'


def test_login():

    with step('Open login page'):
        browser.open('https://demowebshop.tricentis.com/login')

    with step('Fill login form'):
        browser.element('#Email').send_keys(LOGIN)
        browser.element('#Password').send_keys(PASSWORD).press_enter()

    with step ('Varify successful authorization'):
        browser.element('.account').should(have.text(LOGIN))


def test_login_api():

    with step('Login with API'):
        result = requests.post(
            url=API_URL + "/login",
            data={'Email':LOGIN,
                  'Password':PASSWORD,
                  'RememberMe':False},
            allow_redirects=False, #нужен если возврат будет 300-302 код
        )
        allure.attach(body=result.text, name='Response',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')
        allure.attach(body=str(result.cookies), name='Cookies',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')

    with step('Get cookie from API'):
        'кука авторизации которую передадим для авторизации на сайте'
        cookie = result.cookies.get('NOPCOMMERCE.AUTH')

    with step('Set cookie from API'):
        browser.open(url)
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open(url)

    with step ('Varify successful authorization'):
        browser.element('.account').should(have.text(LOGIN))



