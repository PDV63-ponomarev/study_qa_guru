from les9.les9_package.components.panel import LeftPanel
from les9.les9_package.pages.profile_pages import ProfilePage
from les9.les9_package.pages.simple_registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.profile = ProfilePage()
        self.panel = LeftPanel()

app = ApplicationManager()