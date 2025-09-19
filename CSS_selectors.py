from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# start Chrome browser
driver = webdriver.Chrome()


# open the url
driver.get('https://www.amazon.com/')

# CSS selector using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

# $$('.icp-nav-flag. another class') using class

driver.find_element(By.CSS_SELECTOR, '.flex--item.js-terms')

# using attributes $$('[aria-label="Search Amazon"]')

# using tag, class, attribute $$('input.nav-input[dir="auto"]')
# using tag and attribute that contains something $$('input[aria-controls*="autocomplete"]')
