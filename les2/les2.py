import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# настройка драйверов
wep_option = ['--start-maximized', '--disable-gpu']
options = uc.ChromeOptions()
for option in wep_option:
    options.add_argument(option)
driver = uc.Chrome(options=options)

# переход на страницу

driver.get('https://ya.ru')


stroka = driver.find_element(By.CSS_SELECTOR, '[id="text"]')
stroka.send_keys('qa')
stroka.send_keys(Keys.ENTER)
time.sleep(2)

try:
    element = driver.find_element(By.XPATH, f"//*[contains(text(), 'тестировщик')]")
    print("Текст найден:", element.text)
except:
    print("Текст не найден")

driver.quit()