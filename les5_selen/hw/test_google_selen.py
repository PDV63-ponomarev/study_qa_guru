# import undetected_chromedriver as uc
from selene import browser, have, be



def test_google_selen():

    browser.open('')

    # проверка что элемент(окно для текста) пустое
    browser.element('[name="q"]').should(be.blank)

    # ввод текста
    browser.element('[name="q"]').type('some text').press_enter()
    
    browser.element('html').should(have.text('Lorem'))
