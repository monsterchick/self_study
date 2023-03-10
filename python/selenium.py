from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://mega.nz/login')
time.sleep(3)


# input email
email_area = browser.find_element(by=By.NAME,value="login-name2")
email_area.click()
email_area.send_keys("kwanho.app@gmail.com")
time.sleep(1)

# input password
password_area = browser.find_element(by=By.ID,value="login-password2")
password_area.click()
password_area.send_keys("Aa123123.")
time.sleep(1)

# press login button
btn_login = browser.find_element(by=By.XPATH,value="//*[@id=\"login_form\"]/button")
btn_login.click()
time.sleep(10)

# close browser
browser.quit()