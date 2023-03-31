from appium.webdriver.common.appiumby import AppiumBy


class UISelector:
    @classmethod
    def resource_id(cls, resource_id: str):
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{resource_id}")')

    @classmethod
    def text(cls, text: str):
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{text}")')

    @classmethod
    def text_with_scroll(cls, text: str):
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).\
                scrollIntoView(new UiSelector().text("{text}"))')

    @classmethod
    def resource_id_with_scroll(cls, resource_id: str):
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).\
                scrollIntoView(new UiSelector().resourceId("{resource_id}"))')
