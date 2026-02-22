"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=["Desktop", "Mobile"])
def browser_management(request):
    browser.config.base_url = 'https://github.com/'

    if request.param == "Desktop":
        browser.driver.set_window_size(1920, 1080)
    elif request.param == "Mobile":
        browser.driver.set_window_size(375, 812)

    browser.open('')
    yield
    browser.quit()

@pytest.mark.parametrize("browser_management", ["Desktop"], indirect=True)
def test_github_desktop(browser_management):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


@pytest.mark.parametrize("browser_management", ["Mobile"], indirect=True)
def test_github_mobile(browser_management):
    browser.element("//a[contains(@class,'HeaderMenu-link') and contains(., 'Sign in')]").click()
    browser.should(have.url('https://github.com/login'))