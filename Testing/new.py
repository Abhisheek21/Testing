from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://leetcode.com/")
login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
login_btn.click()

wait.until(EC.presence_of_element_located((By.NAME, "login"))).send_keys("abhishekvijayakumar21@gmail.com")
driver.find_element(By.NAME, "password").send_keys("abhishek@2148")
time.sleep(1)
login_button = driver.find_element(By.ID, "signin_btn")
login_button.click()
driver.execute_script("alert('Login Failed!');")
time.sleep(1)
