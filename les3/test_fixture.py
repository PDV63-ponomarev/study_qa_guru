import pytest

@pytest.fixture
def login_page(browser):
    # переход на страницу
    print('page')


@pytest.fixture
def user():
    # фикстура содерж данные
    print('login')
    return 'username', 'password'

def test_login(login_page, user):
    # условный тест поля логин-пароль
    username, password = user
    assert username == 'username'
    assert password == 'password'
    assert 1 != 2

def test_login2(login_page, user):
    # условный тест поля логин-пароль
    username, password = user
    assert username == 'username'
    assert password == 'password'
    assert 1 != 2

