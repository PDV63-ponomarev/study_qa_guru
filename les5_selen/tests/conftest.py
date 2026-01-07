import pytest
from selenium import webdriver
from selene import browser, Browser, Config
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope = 'function',autouse=True)
def browser_managment():
    browser.config.base_url = 'C:/Guru/study_qa_guru/sites/25.html'
    # browser.config.base_url = 'https://www.google.com/'

    # # установка времени поиска, необяз поле
    # browser.config.timeout = 2.0
    #
    # # ввод текст через js, не симуляцией нажатия кнопок
    # browser.config.type_by_js = True

    # скрытый режим, необяз поле
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options

    yield
    browser.quit()

@pytest.fixture(scope = 'function')
def new_browsers():

    # new_browser = Browser(Config(
    #     driver=webdriver.Chrome(
    #         service=ChromeService(
    #             ChromeDriverManager().install()))))

    # yield new_browser
    #
    # new_browser.quit()


    # функция по созданию нового браузера
    future_browsers = []
    def new_browsers(name='chrome'):
        nonlocal future_browsers

        if name == 'chrome':
            fut_browser = (Browser(Config(
                    driver=webdriver.Chrome(service=ChromeService(
                        ChromeDriverManager().install()
                )))))

        elif name == 'firefox':
            fut_browser = (Browser(Config(
                    driver=webdriver.Firefox(service=FirefoxService(
                        GeckoDriverManager().install()
                    )))))

        else:
            raise Exception(f'Browser {name} not supported')

        future_browsers.append(fut_browser)

        return fut_browser

    yield new_browsers

    for fut_browser in future_browsers:
        fut_browser.quit()
