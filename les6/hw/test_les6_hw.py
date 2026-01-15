from datetime import time
from selene import browser, be, have, by
from time import sleep

site = 'C:\project\guru\study_qa_guru\les6\hw\dark_site.html'

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    # текущее время
    current_time = time(hour=23)
    
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    
    # открытие сайта
    browser.open(site)
    
    # переключится на ручной режим
    browser.element('#manualModeOption').click()
    
    if time(6) <= current_time <= time(22):
        # Переключение на светлую тему
        browser.element('#lightThemeBtn').click()
    else:
        browser.element('#darkThemeBtn').click()
    
def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    # открытие сайта
    browser.open(site)
    
    # переключится на ручной режим если надо
    browser.element('#manualModeOption').click()
    
    
    # если автоматический режим включен то
    if browser.element('#autoModeOption').matching(have.css_class('selected')):
        # если время между 6 и 22 включитель
        if time(6) <= current_time <= time(22):
            # должна быть включена светлая тема
            browser.element('[data-theme="light"]')
    
        else:
            # должна быть включена темная тема
            browser.element('[data-theme="dark"]')
            
    # иначе если включен ручной режим        
    elif browser.element('#manualModeOption').matching(have.css_class('selected')):
        
        # по умолчанию включена светлая тема
        browser.element('#alightThemeBtn').matching(have.css_class('active'))
        # браузер по умолчанию должен быть светлый режим
        browser.element('[data-theme="light"]')
        
        # включить темный режим
        browser.element('#darkThemeBtn').click()
        # должна быть включиться темная тема
        browser.element('[data-theme="dark"]')


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    
    for user in users:
        if user['name'] == 'Olga':
            suitable_users = user
    
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
    
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def open_browser(browser_name):
    actual_result = str(open_browser.__name__).replace('_', ' ').title()
    actual_result2 = str(browser_name)
    actual_result = f'{actual_result} [{actual_result2}]'
    
    assert actual_result == "Open Browser [Chrome]"
    


def go_to_companyname_homepage(page_url):
    actual_result = str(go_to_companyname_homepage.__name__).replace('_', ' ').title()
    actual_result2 = str(page_url)
    actual_result = f'{actual_result} [{actual_result2}]'
    
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = str(find_registration_button_on_login_page.__name__).replace('_', ' ').title()
    actual_result2 = str(page_url + ', ' + button_text)
    actual_result = f'{actual_result} [{actual_result2}]'
    
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")
    
    
