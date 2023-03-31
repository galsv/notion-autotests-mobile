from notion_autotests_mobile.model import app
from notion_autotests_mobile.data import test
import allure


@allure.title('Login in Notion app')
def test_login():
    app.auth.login(email=test.email, password=test.password)


@allure.title('Logout from Notion app')
def test_logout():
    app.auth.login(email=test.email, password=test.password)
    app.auth.logout(email=test.email)
