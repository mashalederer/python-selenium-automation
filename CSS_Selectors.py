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
driver.get('https://www.google.com/')

driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

# CSS, class

driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag')

# CSS, class with tag <span is a tag, tags go with <

driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')

## CSS, tag, id, class (order can be different, but tag has to be first)

driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-progressive-attribute')

#CSS attributes we use [], $$('[name="field-keywords"]')

driver.find_element(By.CSS_SELECTOR, '[name="field-keywords"]')
driver.find_element(By.CSS_SELECTOR,  '[data-test="accountNav-signIn"]')


 #CSS, attributes, contains => *= [] $$('[name*="keywords"]')
 #$$('[class*="styles_ndsBaseButton"][class*="styles_filleddefault"][class*="styles_md__X"]')

driver.find_element(By.CSS_SELECTOR, '[name*="keywords"]')



