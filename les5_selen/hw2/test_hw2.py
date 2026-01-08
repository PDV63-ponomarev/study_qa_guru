import time
from selene import browser, be, have
from selenium.webdriver import Keys


def test_form_ru():

    browser.open('/')

    # Ввод первого имени
    browser.element('#firstName').should(be.blank).type('Иван')

    # ввод второго имени
    browser.element('#lastName').should(be.blank).type('Иванов')

    # ввод почты
    browser.element('#userEmail').should(be.blank).type('random@mail.ru')

    # Нажатие кнопки (перекрыто label, нажатие через него)
    browser.element('[for="gender-radio-1"]').click()

    # ввод номера
    browser.element('#userNumber').type('8800123456')

    # ввод даты вручную
    browser.element('#dateOfBirthInput').send_keys(
        Keys.CONTROL + 'a',
        Keys.NULL,
        '01.01.2020',
        Keys.ENTER,
    )

    # проверка сохранения даты
    browser.element('#dateOfBirthInput').should(have.value('01 Jan 2020'))

    # ввод даты нажатием
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(
        '[value="2026"]'
    ).click()
    browser.element('.react-datepicker__month-select').click().element(
        '[value="0"]'
    ).click()
    browser.element(
        '[class="react-datepicker__day react-datepicker__day--001"]'
    ).click()

    # проверка сохранения даты
    browser.element('#dateOfBirthInput').should(have.value('01 Jan 2026'))

    # выбор предметов
    # полный ввод текста
    browser.element('.subjects-auto-complete__control').should(be.blank).type(
        'English'
    ).click(Keys.ENTER)
    # выбор
    browser.element('#subjectsInput').type('biology')
    browser.element('.subjects-auto-complete__option').click()

    # прожатие чекбоксов хобби
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # ввод адреса
    browser.element('#currentAddress').type('Здесь вводится адрес')

    # выбор штата
    browser.all('[class=" css-1wy0on6"]').first.click()
    browser.element('#react-select-3-option-2').click()
    # выбор города
    browser.all('[class=" css-1wy0on6"]').second.click()
    browser.element('#react-select-4-option-0').click()

    # подтверждения
    browser.element('#submit').click()
