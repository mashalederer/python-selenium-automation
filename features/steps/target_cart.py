from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('click on Cart icon')
def input_search(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()
    sleep(4)





@then('see cart is empty')
def see_cart_empty(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text.strip()
    expected_result = "Your cart is empty"
    assert expected_result in actual_result, f"Expected '{expected_result}' but got: '{actual_result}'"