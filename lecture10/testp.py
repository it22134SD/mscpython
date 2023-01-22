from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.python.org')
ps = driver.find_elements(By.TAG_NAME, 'p')
for i, p in enumerate(ps):
    print('---------------------')
    print('Element: %d' %i)
    print(p.text)
    print('---------------------')
