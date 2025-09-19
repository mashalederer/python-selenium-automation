from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# start Chrome browser
driver = webdriver.Chrome()


# open the url
driver.get('https://stackoverflow.com/users/signup')

sleep(5)

# Create you account text
driver.find_element(By.CSS_SELECTOR, '.flex--item.fs-headline1')

# By clicking “Sign up”, you agree to our
# terms of service and acknowledge you have read our privacy policy.
driver.find_element(By.CSS_SELECTOR, '.js-terms')

# email field
driver.find_element(By.ID, "email")

# password field
driver.find_element(By.ID, "password")

# sign up button
driver.find_element(By.ID, 'submit-button')

#Sign up with google
driver.find_element(By.CSS_SELECTOR, '.s-btn__google')

# sign in with git hub
driver.find_element(By.CSS_SELECTOR, '.s-btn__github')

#Collaborate and share knowledge with a private group for FREE.
driver.find_element(By.CSS_SELECTOR, 'a[href*="teams?utm_source=so-owned"]')

