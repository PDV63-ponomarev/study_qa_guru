from selene import have, command
from selene.support.shared import browser
from les9.les9_package import resource

class RegistrationPage:

    # def __init__(self):
        # self.registred_user_data = browser.element('.table').all('td').even


    def open(self):
        browser.open('/automation-practice-form/')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container_]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_second_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def take_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_day_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def take_hobbie(self, hobbies):
        for hobbi in hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobbi)).click()


    def upload_picture(self, file):
        browser.element('#uploadPicture').set_value(resource.path(file))


    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def take_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def take_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def click_submit(self, value):
        browser.element(value).perform(command.js.click)

    def should_registred_user_info(self, *text_find):
        browser.element('.table').all('td').even.should(
            have.exact_texts(*text_find))


