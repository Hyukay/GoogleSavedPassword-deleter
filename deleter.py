from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the web driver
driver = webdriver.Chrome()

# Go to the Google Chrome sign-in page
driver.get('https://accounts.google.com/signin/chrome/sync')

# Enter the email address and password
email_field = driver.find_element(By.ID, 'identifierId')
email_field.send_keys('your_email@example.com')
email_field.submit()
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('your_password')
password_field.submit()

# Go to the passwords page
driver.get('https://passwords.google.com')

# Delete all saved passwords
password_list = driver.find_elements(By.CLASS_NAME, 'password-entry')
for password in password_list:
    password.find_element(By.CLASS_NAME, 'password-entry-delete').click()
    driver.find_element(By.XPATH, '//*[@id="password-delete-confirm"]/div/button[2]').click()

# Close the web driver
driver.close()
