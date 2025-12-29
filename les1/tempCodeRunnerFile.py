from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import csv

options = Options()
cards = None
result = []
pages = True


# во весь экран, оптимизация рендеринга
wep_option = ['--start-maximized', '--disable-gpu']

URL = 'https://books.toscrape.com/'


def get_uc_driver(driver_settings = wep_option) -> webdriver.Chrome:
    # Создание объекта опций с защитой от опр автоматизации
    options = uc.ChromeOptions()

    for option in driver_settings:
        options.add_argument(option)

    driver = uc.Chrome(options=options)
    return driver  


def get_page(URL, driver):
    # переход на страницу
    driver.get(URL)
    
    
    
def find_all_cards(driver):
    global cards
    # находит карточки на странице
    cards = driver.find_elements(By.CLASS_NAME, 'product_pod')

    
  
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
        
    

def find_items_cards(cards):
    
    global result
    #записывает информацию о карточки 
    for product_pod in cards:
        title = product_pod.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        url = product_pod.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
        img = product_pod.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        price = product_pod.find_element(By.CSS_SELECTOR, '.price_color').text

        result.append({
            'title': title,
            'url': url,
            'img': img,
            'price': price
            })
    
    # сохраняет данные в файлы 
    save_doc(result)    


def save_doc(result):
    # пишем в json с отступами
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    
    # читаем json и сохраняем его в csv 
    with open('result.json', 'r', encoding='utf-8') as file:
        result = json.load(file)
        
    with open('result.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['title', 'url', 'img', 'price'])
        for item in result:
            writer.writerow([item['title'], item['url'], item['img'], item['price']])



def main():
    driver: webdriver.Chrome = get_uc_driver()
    get_page(URL, driver)

    while pages == True:
        # Найти карточки
        find_all_cards(driver)
        # записать данные в глобальный список
        find_items_cards(cards)
        # перелистнуть страницу
        page(driver)

    # записать данные из глобал списка в документы
    save_doc(result)
    
    driver.close()

main()
    
