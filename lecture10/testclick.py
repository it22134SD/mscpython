from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.python.org')
button = driver.find_element(By.ID, 'submit')
button.click()
