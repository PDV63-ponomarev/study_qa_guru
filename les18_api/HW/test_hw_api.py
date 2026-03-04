from selene import browser, have
from allure_commons._allure import step
import requests
import allure
from allure_commons.types import AttachmentType
import pytest

LOGIN = 'PDV63@mail.ru'
PASSWORD = 'Passw0rd'

url = 'https://demowebshop.tricentis.com'
LOGIN_URL = f'{url}/login'
CART_URL = f'{url}/addproducttocart/catalog/31/1/1'

@pytest.fixture(scope="session")
def logged_in_session():
    """
    Фикстура, которая создаёт сессию, выполняет регистрацию/логин
    и возвращает сессию с сохранёнными куками.
    """
    session = requests.Session()
    user_data = {
        'Email':LOGIN,
        'Password':PASSWORD,
        'RememberMe':False
    }

    with step('Login form from site'):
        register_response = session.post(
            LOGIN_URL,
            data=user_data,
            allow_redirects=False
        )

    with step('Get status code 302'):
        assert register_response.status_code == 302


    session.get(url)

    return session


def transfer_cookies_to_browser(selenium_driver, requests_session, target_url):
    """
    Переносит все куки из requests.Session() в Selenium браузер
    """
    with step('Open site 1'):
        selenium_driver.get(target_url)

    with step('get cookies'):
        session_cookies = requests_session.cookies.get_dict()

    with step('add login cookies to browser'):
        for cookie_name, cookie_value in session_cookies.items():
            cookie_dict = {
                'name': cookie_name,
                'value': cookie_value,
                'domain': '.demowebshop.tricentis.com',  # Домен для всех поддоменов
                'path': '/',
                'secure': True,
            }
            selenium_driver.add_cookie(cookie_dict)

    with step('Reopen browser from cookies'):
        selenium_driver.refresh()



def test_add_to_cart_after_registration(logged_in_session):
    """
    Тест проверяет, что авторизованный пользователь может добавить товар в корзину.
    """
    with step('add cart cookies to browser'):
        add_to_cart_response = logged_in_session.post(
            CART_URL,
            data={},
            allow_redirects=False)
        result = add_to_cart_response

    with step('get status code 200'):
        assert add_to_cart_response.status_code == 200

    with step('allure logs and cookies'):
        allure.attach(body=result.text,
                      name='Response',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')

        allure.attach(body=str(logged_in_session.cookies.get_dict()),
                      name='Cookies',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')

    with step('Open browser for cookies'):
        browser.open(url)

    with step('Get cookies from browser'):
        transfer_cookies_to_browser(
            selenium_driver=browser.driver,
            requests_session=logged_in_session,
            target_url=url
        )
    with step('Check browser login'):
        browser.element('.account').should(have.text(LOGIN))

    with step('Check browser cart not empty'):
        browser.element('.ico-cart .cart-qty').should(have.no.text('(0)'))


    with step('Get screenshot'):
        allure.attach(
            body=browser.driver.get_screenshot_as_png(),
            name='Cart Screenshot',
            attachment_type=AttachmentType.PNG
        )

