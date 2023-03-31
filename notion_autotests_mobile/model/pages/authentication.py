from selene import browser, be,  have
from appium.webdriver.common.appiumby import AppiumBy
from notion_autotests_mobile.model.controls.uiautomator import UISelector
import allure


class Auth:
    def __init__(self):
        self.input_email = UISelector.resource_id('notion-email-input-1')
        self.input_password = UISelector.resource_id('notion-password-input-2')
        self.button_email = UISelector.text('Continue with email')
        self.button_password = UISelector.text('Continue with password')
        self.navigation_menu = UISelector.resource_id('navigate_to_home')
        self.login_by_email = (AppiumBy.ACCESSIBILITY_ID, 'continue with email')

    def login(self, email: str, password: str):
        with allure.step('Click link "continue with email"'):
            browser.element(self.login_by_email).click()

        with allure.step('Fill email and click button'):
            browser.element(self.input_email).type(email)
            browser.element(self.button_email).click()

        with allure.step('Fill password and click button'):
            browser.element(self.input_password).type(password)
            browser.element(self.button_password).click()

        with allure.step('Should have navigation menu'):
            browser.all(self.navigation_menu).should(have.size_greater_than(0))

    def logout(self, email: str):
        with allure.step('Click button from navigation menu'):
            browser.all(self.navigation_menu).first.click()

        with allure.step('Logout from User context menu'):
            browser.element(UISelector.text(email)).click()
            browser.element(UISelector.text('Log out all')).click()

        with allure.step('Should have start page'):
            browser.element(self.login_by_email).should(be.visible)
