import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")

@when('I open orange HRM Homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('Enter username "{user}" and password "{pwd}"')
def loginParameters(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@when('Click on login button')
def clickLogin(context):
    context.driver.find_element_by_id("btnLogin").click()

@then('User must successfully login to the Dashboard page')
def dashboard(context):
    time.sleep(2)
    try:
        text=context.driver.find_element_by_xpath("//h1[contains(text(), 'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text=="Dashboard":
        context.driver.close()
        assert True, "Test Passed"