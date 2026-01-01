import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# условный фрагмент 
def page(driver):
    # перелистывает страницы
    # ожидание и нажатие кнопки
    global pages
    print('Новая страница')
    try: 
        new_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(., "next")]')))
        new_page.click()
          
    except TimeoutException:
        pages = False
        print('Последняя страница.')

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