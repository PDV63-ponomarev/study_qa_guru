from les9.data import users
from les9.les9_package.pages.application import app


def test_registration_user():
    app.simple_registration.open()

    app.panel.open_text_box()

    app.simple_registration.registration(users.user1)

    app.profile.should_have_data(users.user1)


