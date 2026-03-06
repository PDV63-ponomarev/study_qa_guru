import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # 'app': 'bs://sample.app',
        # 'bstack:options': {
        #     "projectName": "First Python project",
        #     "buildName": "browserstack-build-1",
        #     "sessionName": "BStack first_test",
        #
        #
        #     "userName": "graiwers_wH71Ea",
        #     "accessKey": "MUAc3LgpwMaVd6XQAhYj"
        # }

    })

    browser.config.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                             options=options)
    # browser.config.driver_remote_url = "http://127.0.0.1:4723/wd/hub"
    # browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()