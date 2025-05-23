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
driver.get('https://www.target.com/')

sleep(2)

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]').click()

sleep(2)

#verification

# driver.find_element(By.XPATH, '//div[@data-test="lp-resultsCount"]')
#
# sleep(5)
#
# print("Test case passed")


actual_text = driver.find_element(By.XPATH, '//div[@data-test="lp-resultsCount"]').text
# print('actual text:\n', actual_text)
expected_text = "tea"
assert expected_text in actual_text, f"Error, text{expected_text} not in {actual_text}"
print("Test case passed")