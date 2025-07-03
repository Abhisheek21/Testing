from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Users\abhis\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Leetcode")
driver.get("https://leetcode.com/accounts/login/")
time.sleep(4)
email = "abhishekvijayakumar21@gmail.com"
password = "abhishek@2148"
email_field = driver.find_element(By.XPATH,'//*[@id="id_login"]')
password_field = driver.find_element(By.XPATH,'//*[@id="id_password"]')
email_field.send_keys(email)
password_field.send_keys(password)
login_button = driver.find_element(By.ID, "signin_btn")
login_button.click()
driver.execute_script("alert('Login button clicked!');")
time.sleep(1)
driver.switch_to.alert.accept()
driver.get("https://leetcode.com/")
driver.forward()
driver.back()
driver.refresh()
driver.close()
