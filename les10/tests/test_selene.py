from selene import browser, by, be
from selene.support.shared.jquery_style import s

'''
https://github.com/
eroshenkoam/allure-example

'''



def test_github():
    browser.open('https://github.com/')
    
    s('.header-search-button').click()
    
    browser.element('[name="query-builder-test"]').send_keys('eroshenkoam/allure-example').submit()
    
    s(by.link_text('eroshenkoam/allure-example')).click()
    
    s('[data-content="Pull requests"]').click()
    
    s(by.partial_text('#91')).should(be.visible)