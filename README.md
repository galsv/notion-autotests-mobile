## Test Mobile automation project for Notion
<p align="center">
  <img width="50%" title="Notion" src="notion_autotests_mobile/resources/images/logo_stacks/notion.png">
</p>
Notion is a freemium productivity and note-taking web application developed by Notion Labs Inc. It offers organizational tools including task management, project tracking, to-do lists, bookmarking, and more.

<!-- Technology -->

### Tools and a technologies
<p  align="center">
  <code><img width="5%" title="Pycharm" src="notion_autotests_mobile/resources/images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="notion_autotests_mobile/resources/images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="notion_autotests_mobile/resources/images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Selene" src="notion_autotests_mobile/resources/images/logo_stacks/selene.png"></code>
  <code><img width="5%" title="Selenium" src="notion_autotests_mobile/resources/images/logo_stacks/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="notion_autotests_mobile/resources/images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="notion_autotests_mobile/resources/images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Appium" src="notion_autotests_mobile/resources/images/logo_stacks/appium.png"></code>
  <code><img width="5%" title="Browserstack" src="notion_autotests_mobile/resources/images/logo_stacks/browserstack.png"></code>
  <code><img width="5%" title="Allure Report" src="notion_autotests_mobile/resources/images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="notion_autotests_mobile/resources/images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="notion_autotests_mobile/resources/images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="notion_autotests_mobile/resources/images/logo_stacks/tg.png"></code>
</p>

<!-- Precondition -->

### Configurate Notion before test
* Registration in Browserstack
* Upload your app in Browserstack(I use notion release 0.6.1121)
* Set up Virtual Device Manager with Appium Server and Appium Inspector(for local)
* Run tests and upload app [instruction](https://github.com/qa-guru/mobile-tests-13-py)

<!-- Тest Case -->

### Test cases
* Create/Open/Delete page
* Fill page tittle
* Login and Logout


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="notion_autotests_mobile/resources/images/logo_stacks/jenkins.png"> Run in Jenkins
### [Job](https://jenkins.autotests.cloud/job/notion_mobile_autotests/)
##### Main page of the build:
![This is an image](/notion_autotests_mobile/resources/images/screenshots/jenkins.png)
##### After the build is done the test results are available in Allure Report and Allure TestOps


<!-- Browserstack -->

### <img width="3%" title="Browserstack" src="notion_autotests_mobile/resources/images/logo_stacks/browserstack.png"> Run tests from [Browserstack](https://www.browserstack.com)
##### After starting the build in Jenkins, the tests start running in the Browserstack. You can follow the progress of the test in real time in Browserstack.

![This is an image](/notion_autotests_mobile/resources/images/screenshots/browserstack.png)

##### Configuration .env file for runs from:
##### [browserstack](https://github.com/galsv/notion-autotests-mobile/blob/main/config.personal.env.example)
##### [local](https://github.com/galsv/notion-autotests-mobile/blob/main/config.local.env.example)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="notion_autotests_mobile/resources/images/logo_stacks/allure_report.png"> Allure report
##### Main page of Allure report contains the following blocks:

>- <code><strong>*ALLURE REPORT*</strong></code> - displays date and time of the test, overall number of launched tests,
>- <code><strong>*TREND*</strong></code> - displays trend of running tests for all runs
>- <code><strong>*SUITES*</strong></code> - displays distribution of tests by suites
>- <code><strong>*CATEGORIES*</strong></code> - displays distribution of unsuccessful tests by defect types

![This is an image](notion_autotests_mobile/resources/images/screenshots/allure_dashboard.png)


##### On the page the list of the tests grouped by suites with status shown for each test. Full info about each test can be shown: tags, severity, duration, detailed steps.
![This is an image](notion_autotests_mobile/resources/images/screenshots/allure_suites.png)

##### Test run clip
![This is an image](notion_autotests_mobile/resources/images/screenshots/test_mobile.gif)

<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="notion_autotests_mobile/resources/images/logo_stacks/allure_testops.png"> Allure TestOps Integration
### [Dashboard](https://allure.autotests.cloud/project/2109/dashboards)
##### Results are uploaded there and the automated test-cases can be automatically updated accordingly to the recent changes in the code.
![This is an image](notion_autotests_mobile/resources/images/screenshots/allure_testops_dashboard.png)

Test-cases in the project are imported and constantly updated from the code,
so there is no need in complex process of synchronization manual test-cases and autotests.\
It is enough to create and update an autotest in the code and the test-case in TMS always will be in actual state.\
Manual test-cases also can be added in TMS in case of need(via web interface or via code).

![This is an image](notion_autotests_mobile/resources/images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="notion_autotests_mobile/resources/images/logo_stacks/jira.png"> Jira integration
##### After configuration TestOps we can integrate results launches in Jira

![This is an image](notion_autotests_mobile/resources/images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="notion_autotests_mobile/resources/images/logo_stacks/tg.png"> Telegram Notifications
##### Telegram bot sends a brief report to a specified telegram chat by results of each build.

![This is an image](notion_autotests_mobile/resources/images/screenshots/tg_bot.png)
