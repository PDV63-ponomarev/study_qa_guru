import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

@pytest.fixture(scope='session')
def open_browser():
    wep_option = ['--start-maximized', '--disable-gpu']
    options = uc.ChromeOptions()
    for option in wep_option:
        options.add_argument(option)
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def page(open_browser):
    driver = open_browser
    driver.get('https://ya.ru')
    return driver

def test_give_text(page):
    driver = page
    stroka = driver.find_element(By.CSS_SELECTOR, '[id="text"]')

    assert stroka, 'Строка поиска не найдена'

    

def test_find_text(page):

    driver = page
    stroka = driver.find_element(By.CSS_SELECTOR, '[id="text"]')

    stroka.send_keys('qa')
    stroka.send_keys(Keys.ENTER)
    sleep(2)
    element = driver.find_element(By.XPATH, f"//*[contains(text(), 'тестировщик')]")
    
    assert element, 'Текст не найден'

    print(f'Текст найден')



def test_find_badtext(page):
    driver = page
    stroka = driver.find_element(By.CSS_SELECTOR, '[id="text"]')

    stroka.send_keys('STUDENTS')
    stroka.send_keys(Keys.ENTER)

    assert len(driver.find_elements(By.XPATH, "//*[contains(text(), 'тестировщик')]")) == 0
   
    print(f'Плохой текст не найден')