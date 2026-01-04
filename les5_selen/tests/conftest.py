import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope = 'function',autouse=True)
def browser_managment():
    browser.config.base_url = 'C:/Guru/study_qa_guru/sites/25.html'
    # browser.config.base_url = 'https://www.google.com/'
    
    # установка времени поиска, необяз поле
    browser.config.timeout = 2.0

    # скрытый режим, необяз поле
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    yield
    browser.quit()