import pytest
from selene import browser
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope='function', autouse=True)
def browser_managment():

    # Настройки Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')

    # Отключить ожидание полной загрузки страницы
    chrome_options.page_load_strategy = 'eager'

    # Создаем undetected драйвер
    driver = uc.Chrome(
        options=chrome_options,
        headless=True,  # False или True для headless
        use_subprocess=True,  # для стабильности
    )

    # Настраиваем Selene
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    # Устанавливаем размер окна
    # driver.maximize_window()

    yield

    browser.quit()
