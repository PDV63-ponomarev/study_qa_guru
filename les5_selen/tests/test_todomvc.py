from curses.ascii import ACK

from selene import browser, command, have, be
from time import sleep

from selenium.webdriver import ActionChains, Keys


def test_add_todos_and_complete_one():

    browser.open('')

    # проверка с ожиданием что заголовок имеет название
    # код не падает в случае несоответсвия
    if browser.wait_until(have.title('TodoMvc')):
        print('Some text')
    else:
        print('some text2')

    # проверка без ожидания что заголовок имеет название
    # код не падает в случае несоответсвия
    if browser.matching(have.title('TodoMvc')):
        print('Some text')
    else:
        print('some text2')


# нажатие нескольких кнопок
actions = ActionChains(browser.driver)
# после зажатия всегда надо отжимать зажатые
actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
# или
browser.element('#new-todo').type(Keys.COMMAND + 'a' + Keys.NULL)
browser.element('#new-todo').type(Keys.COMMAND + 'a' + Keys.NULL + 'some text')
# или
browser.element('#new-todo').send_keys(
    Keys.CONTROL + 'a',
    Keys.NULL,
    'some text',
)


# заморозка пропадаюших окон
# в консоле браузера ввести setTimeout('debugger', 3000)
# через заданное время заморозится экран и вспл окна
