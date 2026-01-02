import pytest

@pytest.fixture(scope='session')
def browser():
    # открытие браузера
    print('browser open')


    #  по завершению возврат к этому    
    # если тест упал то код все равно выполнится
    yield 
    print('browser close')