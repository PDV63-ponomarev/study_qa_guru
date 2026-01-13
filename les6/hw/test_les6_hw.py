from datetime import time
from selene import browser, be, have, by
from time import sleep

site = 'C:\project\guru\study_qa_guru\les6\hw\dark_site.html'

# def test_dark_theme_by_time():
#     """
#     Протестируйте правильность переключения темной темы на сайте в зависимости от времени
#     """
#     # текущее время
#     current_time = time(hour=23)
    
#     # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    
#     # открытие сайта
#     browser.open(site)
    
#     # переключится на ручной режим
#     browser.element('#manualModeOption').click()
    
#     if time(6) <= current_time <= time(22):
#         # Переключение на светлую тему
#         browser.element('#lightThemeBtn').click()
#     else:
#         browser.element('#darkThemeBtn').click()
    
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

    