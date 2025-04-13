from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when("Search for tea")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]').click()
    sleep(6)


@then('Verify correct search results shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, '//div[@data-test="lp-resultsCount"]').text
    expected_text = "tea"
    assert expected_text in actual_text, f"Error, text{expected_text} not in {actual_text}"


@then("click on the cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    sleep(1)

@then('Verify your cart is empty')
def verify_empty_cart(context):
    actual_result = context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]').text
    expected_result = "Your cart is empty"
    assert actual_result == expected_result, f"Error, {actual_result} != {expected_result}"
    sleep(1)


@then('Select to sign in')
def select_sign_in(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(2)


@then('Click Sign in or Create account button')
def sign_in_button(context):
    context.driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()
    sleep(2)


@then('Verify Sign in page is open')
def verify_sign_in_page(context):
    actual_text = context.driver.find_element(By.XPATH, '//h1[contains(text(), "Sign in or create account")]').text
    expected_text= 'Sign in or create account'
    assert expected_text in actual_text, f"Error, text{expected_text} not in {actual_text}"
    sleep(1)
