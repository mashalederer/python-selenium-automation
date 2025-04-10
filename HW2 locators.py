# Amazon logo
driver.find_element(By.ID, 'nav-logo-sprites')

# Email field
driver.find_element(By.ID, 'ap_email')


# Continue button
driver.find_element(By.ID, 'continue')


# Conditions of use link

driver.find_element(By.XPATH, '//a[contains(@href, "gp/help/customer/display.html") and text()="Conditions of Use"]'



# Privacy Notice link

driver.find_element(By.XPATH, '//a[contains(@href, "gp/help/customer/display.html") and text()="Privacy Notice"]'

# Need help link

driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]'


# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')


# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

