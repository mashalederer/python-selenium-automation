from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')

@when('click on sign in button')
def input_search(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(2)

@when('From right side navigation menu click sign in button')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()
    sleep(3)

@then('Sign In form opened')
def open_sign_in(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD').text.strip()
    expected_result = "Sign in or create account"
    assert expected_result in actual_result, f"Expected '{expected_result}' but got: '{actual_result}'"