import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s

'''
https://github.com/
eroshenkoam/allure-example

'''



def test_dynamic_github():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-button').click()
        browser.element('[name="query-builder-test"]').send_keys('eroshenkoam/allure-example').submit()

    with allure.step('Проходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем requests'):
        s('[data-content="Pull requests"]').click()

    with allure.step('Проверяем наличие requests 91'):
        s(by.partial_text('#91')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_depository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_requests()
    should_see_number('#91')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')

@allure.step('Ищем репозиторий {repo}')
def search_for_depository(repo):
    s('.header-search-button').click()
    (browser.element('[name="query-builder-test"]').
     send_keys(repo).submit())

@allure.step('Проходим по ссылке репозитория')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем requests')
def open_requests():
    s('[data-content="Pull requests"]').click()


@allure.step('Проверяем наличие requests 91')
def should_see_number(repo):
    s(by.partial_text(repo)).should(be.visible)