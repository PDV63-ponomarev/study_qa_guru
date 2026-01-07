from selene import browser, be

def test_complete_todo(new_browsers):

    browser.open('')
    browser.element('#message').should(be.blank)
    browser.element('#message').type('some text')

    # browser2 = new_browser

    browser2 = new_browsers()
    browser2.open('C:/Guru/study_qa_guru/sites/25.html')
    browser2.element('#message').type('ANOTHER text')

    browser3 = new_browsers('firefox')
    browser3.open('C:/Guru/study_qa_guru/sites/25.html')
    browser3.element('#message').type('MORE text')