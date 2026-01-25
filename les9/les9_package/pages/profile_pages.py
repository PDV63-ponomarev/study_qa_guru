from selene import have, by
from selene.support.shared import browser

from  les9.data.users import User


class ProfilePage:

   def should_have_data(self, user: User):
        output = browser.element('#output')
        output.should(have.text(f'Name:{user.full_name}'))
        output.should(have.text(f'Email:{user.email}'))
        output.should(have.text(f'Current Address :{user.address}'))

