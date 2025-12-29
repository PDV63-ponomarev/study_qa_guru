from selene import browser, be, have
from time import sleep


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
browser.element('html').should(have.text('About this page'))
sleep (2)

# browser.element('[id="search"]').should(have.text('QA.GURU: Курсы тестировщиков'))