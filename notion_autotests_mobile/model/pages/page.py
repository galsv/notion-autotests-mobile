from selene import browser, be, have
from appium.webdriver.common.appiumby import AppiumBy
from notion_autotests_mobile.model.controls.uiautomator import UISelector
from notion_autotests_mobile.data import test
from notion_autotests_mobile.model.controls import key_code
import allure
import time


class Page:
    def __init__(self):
        self.navigation_menu = UISelector.resource_id('navigate_to_home')

    def open(self, page_name: str):
        with allure.step('Click button from navigation menu'):
            browser.all(self.navigation_menu).first.click()
            browser.element(UISelector.text(test.email)).should(be.visible)
            browser.element(UISelector.resource_id_with_scroll(f'page_row_{page_name}')).should(be.visible).click()

        with allure.step('Should opened page'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Web view')).should(be.visible)

    def create(self, page_name: str):
        with allure.step('Click button from navigation menu'):
            browser.all(self.navigation_menu).first.click()
            browser.element(UISelector.text(test.email)).should(be.visible)
            browser.all(self.navigation_menu)[-1].click()

        with allure.step('Fill title and should result'):
            key_code.fill_text_by_keycode(page_name)
            key_code.press_enter()
            browser.element(UISelector.text(page_name)).should(be.visible)
            time.sleep(1)

    def delete_by_name(self, page_name: str):
        with allure.step('Click button from navigation menu'):
            browser.all(self.navigation_menu).first.click()
            browser.element(UISelector.text(test.email)).should(be.visible)

        with allure.step('Click context menu by page name'):
            browser.element(UISelector.resource_id_with_scroll(f'page_row_{page_name}'))\
                .all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[1].click()

        with allure.step('Click delete button'):
            browser.element(UISelector.text('Delete')).click()
            browser.all(self.navigation_menu).should(have.size_greater_than(0))
