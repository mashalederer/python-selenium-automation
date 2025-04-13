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

driver.get('https://www.amazon.com')


# by id

driver.find_element(By.ID, 'twotabsearchtextbox')
deiver.find_element(By.ID, 'nav-search-submit-button')

#by Xpath

driver.find_element(By.XPATH, '//input[@aria-label="Search Amazon"]')

#by Xpath, multiple attributes

driver.find_element(By.XPATH, '//input[@tabindex="0" and @name="field-keywords"]')


#by Xpath, any tag

driver.find_element(By.XPATH, '//*[@tabindex="0" and @name="field-keywords"]')

# by Xpath, using text $x("//h1[contains(text(),'Create account')]")

driver.find_element(By.XPATH, '//a[text()="Best Sellers" and @class="nav-a  "]')

# by Xpath, using partial text match


driver.find_element(By.XPATH, '//a[contains(text()="Best")]')

# by Xpath using several attributes

driver.find_element(By.XPATH, '//select[contains(aria-describedby, class)]')
