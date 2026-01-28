import allure
from selene import browser, by, be
from selenium.webdriver import Keys


# Чистый Selene (без шагов)
def test_github_only_selene():

    browser.open('https://github.com/')

    browser.element(('.header-search-button')).click()

    browser.element('[name="query-builder-test"]').send_keys('eroshenkoam/allure-example')
    browser.element('[name="query-builder-test"]').submit()
    # browser.element('[name="query-builder-test"]').send_keys((Keys.ENTER))

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('[data-content="Pull requests"]').click()

    browser.element(by.partial_text('#91')).should(be.visible)



# Лямбда шаги через with allure.step
def test_github_with_allure():

    with allure.step('Open browser'):
        browser.open('https://github.com/')

    with allure.step('Fill for the search string'):
        browser.element(('.header-search-button')).click()

    with allure.step('Give search text with press ENTER'):
        browser.element('[name="query-builder-test"]').send_keys('eroshenkoam/allure-example')
        browser.element('[name="query-builder-test"]').submit()
        # browser.element('[name="query-builder-test"]').send_keys((Keys.ENTER))

    with allure.step('Fill needs text'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Go to Pull requests'):
        browser.element('[data-content="Pull requests"]').click()

    with allure.step('Should needs number'):
        browser.element(by.partial_text('#91')).should(be.visible)


# Шаги с декоратором @allure.step

@allure.step('Open browser')
def open_browser(site):
    browser.open(site)

@allure.step('Fill for the search string')
def fill_search():
    browser.element('.header-search-button').click()

@allure.step('Give search text with press ENTER')
def give_search_text(text):
    browser.element('[name="query-builder-test"]').send_keys(text)
    browser.element('[name="query-builder-test"]').submit()
    # browser.element('[name="query-builder-test"]').send_keys((Keys.ENTER))

@allure.step('Fill needs text')
def get_search_string(text):
    browser.element(by.link_text(text)).click()

@allure.step('Go to Pull requests')
def go_to_step():
    browser.element('[data-content="Pull requests"]').click()

@allure.step('Should needs number')
def should_number(num):
    browser.element(by.partial_text(num)).should(be.visible)

def test_github_with_allure_fixtures():
    open_browser('https://github.com/')
    fill_search()
    give_search_text('eroshenkoam/allure-example')
    get_search_string('eroshenkoam/allure-example')
    go_to_step()
    should_number('#91')