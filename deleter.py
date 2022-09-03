from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Open the browser
browser = webdriver.GoogleChrome()

# Open google account settings passwords
browser.get('chrome://settings/passwords')

# Find the delete button for each saved password
delete_buttons = browser.find_elements(By.XPATH, '//button[@aria-label="Delete"]')


# Click the delete button for each saved password
for button in delete_buttons:
    button.click()




