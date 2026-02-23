"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have

@pytest.fixture(params=["Desktop", "Mobile"])
def browser_management(request):
    browser.config.base_url = 'https://github.com/'

    browser.open('')

    if request.param == "Desktop":
        browser.driver.set_window_size(1920, 1080)
    elif request.param == "Mobile":
        browser.driver.set_window_size(375, 812)


    yield request.param
    browser.quit()


def test_github_desktop(browser_management):
    if browser_management == "Mobile":
        pytest.skip('Мобильное расшерение')

    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))

def test_github_mobile(browser_management):
    if browser_management == "Desktop":
        pytest.skip("Десктопное расшерение")

    browser.element("//a[contains(@class,'HeaderMenu-link') and contains(., 'Sign in')]").click()
    browser.should(have.url('https://github.com/login'))