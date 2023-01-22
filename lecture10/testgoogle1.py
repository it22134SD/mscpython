#---import
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import configparser

USERNAME = 'testuser1@hua.gr'
ACCEPT_TERMS = 'Αποδοχή όλων'
USER_GREETINGS = 'James Kirk'
PASSWORD_FILE = 'password.conf'

config = configparser.ConfigParser()
config.read(PASSWORD_FILE)
password = config['DEFAULT']['password']

#---config
driver = webdriver.Firefox()
driver.get('https://www.google.com')
time.sleep(2)
buttons = driver.find_elements(By.ID, 'L2AGLb')
assert len(buttons) == 1
select = buttons[0]
select.click()

#---accept
links = driver.find_elements(By.LINK_TEXT, 'Είσοδος')
assert len(links) == 1
select = links[0]
select.click()

username_elements = driver.find_elements(By.ID, 'identifierId')
assert len(username_elements) == 1
select = username_elements[0]
select.send_keys(USERNAME)

next_elements = driver.find_elements(By.ID, 'identifierNext')
assert len(next_elements) == 1
select = next_elements[0]
select.click()
#---password

time.sleep(5)
assert "Harokopio" in driver.title

select = driver.find_element(By.ID, 'username')
select.send_keys(USERNAME)
select = driver.find_element(By.ID, 'password')
select.send_keys(password)
button = driver.find_element(By.ID, 'submit_button')
button.click()
#---sso

alerts = driver.find_elements(By.CLASS_NAME, 'alert')
assert 0 == len(alerts)

time.sleep(5)

driver.get('https://accounts.google.com')
h1 = driver.find_element(By.TAG_NAME,'h1')
time.sleep(5)
assert USER_GREETINGS in h1.text
#---accounts
