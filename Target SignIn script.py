# Test Case: Users can navigate to SignIn page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. Open https://www.target.com/
driver.get('https://www.target.com/')

sleep(2)

# 2. Click SignIn button

driver.find_element(By.ID, 'account-sign-in').click()

sleep(2)

# 3. Click SignIn from side navigation

driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()

sleep(2)

# 4. Verify SignIn page opened:
# “Sign into your Target account” text is shown,

expected_text= 'Sign in or create account'

actual_text = driver.find_element(By.XPATH, '//h1[contains(text(), "Sign in or create account")]').text

assert expected_text in actual_text, f"Error, text{expected_text} not in {actual_text}"
print("SignIn page opened, test case passed")

# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

sign_in_button_present = driver.find_element(By.ID, "login")
assert sign_in_button_present is not None, "SignIn button not found!"

print("SignIn button is shown, test case passed")

sleep(5)
driver.quit()


