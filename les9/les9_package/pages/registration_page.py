from selene import have, command
from selene.support.shared import browser


class RegistrationPage:

    # def __init__(self):
    #     self.registred_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('/automation-practice-form/')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container_]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_day_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    # @property
    # def registred_user_data(self):
    #     return browser.element('.table').all('td').even

    def should_registred_user_info(self, *text_find):
        browser.element('.table').all('td').even.should(
            have.exact_texts(*text_find))
