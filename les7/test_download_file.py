import os
import requests
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import query
from time import sleep

from les7.script_os import TMP_DIR

def test_text_in_download_file():
        
    # код для указания пути скач файла и автом подтверждение скачивания 
    options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': TMP_DIR,
        'download.promt_for_download': False
    }
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver
    
    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')

    # #скачивание через ссылку
    download_url = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))
    content = requests.get(url=download_url).content
    with open(os.path.join(TMP_DIR, 'readme2.rts'), 'wb') as file:
        file.write(content)


    # скачивание через кнопку
    browser.element('[data-testid="download-raw-button"]').click()

    # проверка что файл содержит test_answer
    with open(r'tmp\readme2.rst') as file:
        file_content = file.read()
        assert 'test_answer' in file_content