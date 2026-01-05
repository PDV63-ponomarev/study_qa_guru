from selene import browser, command, have, be
from time import sleep

# def test_complete_todo():

#     browser.open('')

#     # проверка что элемент(окно для текста) пустое
#     browser.element('#message').should(be.blank)

#     # ввод текста
#     browser.element('#message').type('some text').press_enter()
#     browser.element('#message').type('some text2').press_enter()

#     # выделить текст
#     browser.element('#message').perform(command.select_all)
#     sleep(3)

#     element = '.form-container>#checkboxForm>.form-group>.form-check'
    
#     # проверка что 5 элементов в графе люб еда, вручную указывает таймоут
#     browser.all(element).with_(timeout=4.0).should(have.size(5))

#     # просто ожидание пока...
#     browser.all(element).wait.for_(have.size(5))


def test_dubl():
    browser.open('')

    # проверка что элемент(окно для текста) пустое
    browser.element('#message').should(be.blank)

    # ввод текста
    browser.element('#message').type('some text').press_enter()
    browser.element('#message').type('some text2').press_enter()


    element = '.form-container>#checkboxForm>.form-group>.form-check'
    # проверка что 5 элементов в графе люб еда, вручную указывает таймоут
    browser.all(element).should(have.size(5))

    # поиск по xpath
    element_xpath = '//*[@class="form-container"]/[@id=checkboxForm]/[@class=form-group]/[@class=form-check]'
    browser.element(element_xpath)

    # проверка что элемент содержит такой текст
    browser.all(element).first.should(have.exact_text('Пицца'))
    browser.all(element).second.should(have.exact_text('Бургер'))
    browser.all(element)[2].should(have.exact_text('Суши'))
    browser.all(element)[-1].should(have.exact_text('Салат'))

    browser.all(element).should(have.exact_texts('Пицца','Бургер',
                                                 'Суши','Такос','Салат'))
    

    # клик чекбокса
    browser.all(element).first.element('[type="checkbox"]').click()
    browser.all(element).element_by(have.exact_text('Бургер')).element('[type="checkbox"]').click()

    # проверяет что все элементы с классом сост из текста (лишних кликов нет)
    browser.all(element).by(have.css_class('completed')).should(have.exact_texts('Пицца','Бургер'))

    browser.all(element).by(have.no.css_class('completed')).should(have.exact_texts('Суши','Такос','Салат'))


 

