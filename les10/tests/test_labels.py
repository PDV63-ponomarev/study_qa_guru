import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity



def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задача в репозитории')
    allure.dynamic.story('Пользователь не может создать задачу')
    allure.dynamic.link('https://github.com/', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'eroshenko')
@allure.feature('Задача')
@allure.story('Авторизированный пользователь может создать задачу и репозитогрий')
@allure.link('https://github.com/', name='Testing')
def test_decorator_labels():
    pass