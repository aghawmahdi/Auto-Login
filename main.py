from selenium import webdriver
import time

username = "your username"
password = "your password"

url = "your login page"

driver = webdriver.Safari()
driver.get(url)

driver.find_element_by_id("id_email").send_keys(username)
driver.find_element_by_id("id_password").send_keys(password)
driver.find_element_by_name("sign_in_submit").click()

print("Done")
time.sleep(1)

