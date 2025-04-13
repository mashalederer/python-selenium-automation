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

# open the url
driver.get('https://www.amazon.com/')



# Amazon logo

driver.find_element(By.CSS_SELECTOR,  '[class*="a-icon-logo"][role="presentation"]')


# Create account

driver.find_element(By.XPATH, "//h1[contains(text(),'Create account')]")

# your name field

driver.find_element(By.ID,  "ap_customer_name")

# email field

driver.find_element(By.ID, "ap_email")

# password field

driver.find_element(By.ID, "ap_password")

# re-enter password field

driver.find_element(By.ID,  "ap_password_check")

# Create Amazon account button

driver.find_element(By.ID, "auth-continue-announce"]')

# Conditions of use

driver.find_element(By.XPATH, '//a[text()="Conditions of Use" and contains(@href, "ap_register_notification_condition_of_use")]')


# Privacy Notice

driver.find_element(By.XPATH, '//a[text()="Privacy Notice" and contains(@href, "ap_register_notification_privacy_notice")]')


driver.find_element(By.CSS_SELECTOR,[class*="a-link-emphasis"][href*="ap/signin?openid.pape.max_auth_age=0&openid.return_to"]')
