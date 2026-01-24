

from les9.les9_package.pages.registration_page import RegistrationPage


def test_form_light_oop():

    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Olga')
    registration_page.fill_second_name('YA')
    registration_page.fill_email('name@example.com')

    registration_page.take_gender('Female')

    registration_page.fill_number('1234567891')

    registration_page.fill_day_of_birth('1999', 'May', '11')

    registration_page.fill_subject('Computer Science')

    registration_page.take_hobbie('Reading')

    registration_page.upload_picture('foto.jpg')

    registration_page.fill_address('Moscowskaya Street 18')

    registration_page.take_state('NCR')

    registration_page.take_city('Delhi')

    registration_page.click_submit('#submit')


    # THEN
    registration_page.should_registred_user_info(
        'Olga YA',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi',)