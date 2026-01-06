import pytest
from selene import browser

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope = 'function',autouse=True)
def browser_managment():

    # Настройки Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')

    
    # Создаем undetected драйвер
    driver = uc.Chrome(
        options=chrome_options,
        headless=False,  # или True для headless
        use_subprocess=True,  # важно для стабильности
    )
    
    # Настраиваем Selene
    browser.config.driver = driver
    browser.config.base_url = 'https://www.google.com'
    driver.maximize_window()

    yield
    browser.quit()


