from les9.les9_package.pages.registration_page_high import RegistrationPageHigh

user1 = {'firstName': 'Иван',
        'lastName': 'Иванов',
        'email': 'random@mail.ru',
        'gender': 'Male',
        'number': '8800123456',
        'day_of_birth': ('2026', 'January', '01'),
        'subject': 'English',
        'hobbies': ('Sports', 'Reading', 'Music'),
        'photo': 'foto.jpg',
        'addres': 'Россия, г. Мытищи, Ленинская ул., д. 16 кв.194',
        'state': 'Haryana',
        'city': 'Karnal',
         }

def test_site_oop_high():

    registration_page = RegistrationPageHigh(user1)
    registration_page.open()

    registration_page.register()

    registration_page.should_registred_user_info(user1)