import allure
import allure_commons
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selene import browser
from selene import support
from appium import webdriver

import config
from notion_autotests_mobile import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    appium_driver_options = config.settings.driver_options

    # hide keyboard
    appium_driver_options.set_capability("unicodeKeyboard", True)
    appium_driver_options.set_capability("resetKeyboard", True)

    # It doesn't work with browserstack, only local
    # if config.settings.run_on_browserstack:
    #     appium_driver_options.set_capability('noReset', no_reset)
    # else:
    #     appium_driver_options.no_reset = no_reset

    with allure.step('Set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=appium_driver_options
        )

    yield

    if config.settings.run_on_browserstack and request.node.result_of_call.failed:
        utils.allure.attach.screenshot(name='Last screenshot')
        utils.allure.attach.screen_xml_dump()

    session_id = browser.driver.session_id

    allure.step('Close app session')(browser.quit)()

    if config.settings.run_on_browserstack:
        utils.allure.attach.video_from_browserstack(session_id)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):  # noqa
    # execute all other hooks to obtain the report object
    outcome = yield
    result_of_ = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, 'result_of_' + result_of_.when, result_of_)
