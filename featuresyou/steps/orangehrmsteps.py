from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")

@when(u'open orange hrm home')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath(
        "//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
