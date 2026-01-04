from selene import browser, have, be

def test_complete_todo():

    browser.open('')

    # проверка что элемент(окно для текста) пустое
    browser.element('#message').should(be.blank)

    # ввод текста
    browser.element('#message').type('some text').press_enter()
    browser.element('#message').type('some text2').press_enter()


    element = '.form-container>#checkboxForm>.form-group>.form-check'
    
    # проверка что 5 элементов в графе люб еда, вручную указывает таймоут
    browser.all(element).with_(timeout=4.0).should(have.size(5))

    # просто ожидание пока...
    browser.all(element).wait.for_(have.size(5))