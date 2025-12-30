import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# настройка драйверов
wep_option = ['--start-maximized', '--disable-gpu']
options = uc.ChromeOptions()
for option in wep_option:
    options.add_argument(option)
driver = uc.Chrome(options=options)

# переход на страницу

driver.get('https://google.com')


stroka = driver.find_element(By.NAME, 'q')
stroka.send_keys('qa.guru')
stroka.send_keys(Keys.ENTER)

try:
    element = driver.find_element(By.XPATH, f"//*[contains(text(), 'Освойте тестирование ПО с нуля')]")
    print("Текст найден:", element.text)
except:
    print("Текст не найден")

driver.quit()