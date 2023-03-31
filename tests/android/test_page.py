from notion_autotests_mobile.model import app
from notion_autotests_mobile.data import test
import allure


@allure.title('Create new page')
def test_create():
    app.auth.login(email=test.email, password=test.password)
    app.page.create(test.page_name)


@allure.title('Open page by name')
def test_open():
    app.auth.login(email=test.email, password=test.password)
    app.page.open(test.page_name)


@allure.title('Delete page by name')
def test_delete():
    app.auth.login(email=test.email, password=test.password)
    app.page.delete_by_name(test.page_name)
