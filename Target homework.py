from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()



# # open the url
driver.get('https://www.target.com/')
driver.find_element(By.XPATH, '//*[text()="Account"]').click()
sleep(3)
driver.find_element(By.XPATH, '//*[@data-test="accountNav-signIn"]').click()
sleep(3)



actual_result = driver.find_element(By.XPATH, '//*[text()="Sign in or create account"]').text

expected_result = "Sign in or create account"
assert expected_result in actual_result

print("test passed")
sleep(5)

