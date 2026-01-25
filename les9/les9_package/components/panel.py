from selene import have, by
from selene.support.shared import browser

from les9.les9_package.pages.profile_pages import ProfilePage


class LeftPanel:
    def __init__(self):
        self.panel= browser.element('.left-pannel')

    def open(self, item):
        self.panel.element(by.text(item)).click()

    def open_text_box(self):
        self.open('Text Box')
        return ProfilePage()