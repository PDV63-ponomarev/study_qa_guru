from selene import have, command
from selene.support.shared import browser
from les9.les9_package.pages import registration_page
from les9.les9_package.pages.registration_page import RegistrationPage


class RegistrationPageHigh:

    def __init__(self, user_data=None):

        self.first_name = user_data.get('firstName')
        self.lastName = user_data.get('lastName')
        self.email = user_data.get('email')
        self.gender = user_data.get('gender')
        self.number = user_data.get('number')
        self.day_of_birth = user_data.get('day_of_birth')
        self.subject = user_data.get('subject')
        self.hobbies = user_data.get('hobbies')
        self.photo = user_data.get('photo')
        self.addres = user_data.get('addres')
        self.state = user_data.get('state')
        self.city = user_data.get('city')


    def open(self):
        browser.open('/automation-practice-form/')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container_]').perform(command.js.remove)


    def register(self):

        registration_page = RegistrationPage()

        registration_page.fill_first_name(self.first_name)
        registration_page.fill_second_name(self.lastName)
        registration_page.fill_email(self.email)

        registration_page.take_gender(self.gender)

        registration_page.fill_number(self.number)

        registration_page.fill_day_of_birth(*self.day_of_birth)

        registration_page.fill_subject(self.subject)

        registration_page.take_hobbie(self.hobbies)

        registration_page.upload_picture(self.photo)

        registration_page.fill_address(self.addres)

        registration_page.take_state(self.state)

        registration_page.take_city(self.city)

        registration_page.click_submit('#submit')



    def should_registred_user_info(self, user_data):
        expected_data = [
            f"{user_data['firstName']} {user_data['lastName']}",  # Имя и фамилия вместе
            user_data['email'],
            user_data['gender'],
            user_data['number'],
            f"{user_data['day_of_birth'][2]} {user_data['day_of_birth'][1]},{user_data['day_of_birth'][0]}",
            # 01 January,2026
            user_data['subject'],
            ', '.join(user_data['hobbies']),  # Sports, Reading, Music
            user_data['photo'],
            user_data['addres'],
            f"{user_data['state']} {user_data['city']}"  # Haryana Karnal
        ]

        browser.element('.table').all('td').even.should(
            have.exact_texts(*expected_data)  # распаковываем список
        )
