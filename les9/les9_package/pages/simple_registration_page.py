from selene.support.shared import browser
from les9.data.users import User

class SimpleRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.address = browser.element('#currentAddress')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/checkbox')

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_address(self, value):
        self.address.type(value)

    def submit1(self):
        self.submit.click()


    def should_have_submited(self, full_name, email, address):
        pass

    def registration(self, user: User):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_address(user.address)
        self.submit1()
