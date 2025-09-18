from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Create locators + search strategy for these page elements of Amazon Sign in page:
# Amazon logo
driver.find_element(By.ID, "a-icon a-icon-logo")


# Email field
driver.find_element(By.ID, "ap_email_login")

# Continue button
driver.find_element(By.ID, "continue-announce")
# Conditions of use link

driver.find_element(By.XPATH, '//*[text()="Conditions of Use"]')

# Privacy Notice link
driver.find_element(By.XPATH, '//*[text()="Privacy Notice"]')

# Need help link
driver.find_element(By.XPATH, '//*[@role="button"]')


# the interface changed on Amazon website i cant find the following:
# Forgot your password link
# Other issues with Sign-In link
# Create your Amazon account button
# but there is Create a free business account and locator will be

driver.find_element(By.ID, 'ab-registration-ingress-link')

# help link
driver.find_element(By.XPATH, '//*[@href="/help"]')




# #########################################################################################
# please ignore this part, it is just my notes i like to make when i watch lessons online

driver.find_element(By.ID, )


# find by XPATH
driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon"]')
driver.find_element(By.XPATH, '//input[@aria-label="Search Amazon""]')
driver.find_element(By.XPATH, '//input[@name="field-keywords"]')

# XPath, many attributes
driver.find_element(By.XPATH, '//input[@type="text" and @dir="auto"]')

# XPath, text()
driver.find_element(By.XPATH, '//a[text()="Best Sellers"]')

# XPath text() combined with attribute $x('//a[text()="Best Sellers" and @class="nav-a  "]')

driver.find_element(By.XPATH, '//a[text()="Best Sellers" and @class="nav-a  "]')

# XPath with any tag with * $x('//*[@data-csa-c-content-id="nav_cs_all_books"]')
# * means any tag

driver.find_element (By.XPATH, '//*[@data-csa-c-content-id="nav_cs_all_books"]')

# XPath parent => child node $x('//div[@class="nav-div"]//a[text()="Best Sellers"]')

driver.find_element(By.XPATH, '//div[@class="nav-div"]//a[text()="Best Sellers"]')

#XPath with contains $x('//a[text()="Best Sellers" and contains(@href, "nav_cs_bestsellers")]')

driver.find_element(By.XPATH, '//a[text()="Best Sellers" and contains(@href, "nav_cs_bestsellers")]')
