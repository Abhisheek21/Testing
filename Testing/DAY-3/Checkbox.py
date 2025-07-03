from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://demoqa.com/automation-practice-form')
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkbox = browser.find_element(By.XPATH,'//*[@id="hobbiesWrapper"]/div[2]/div[1]/label')
checkbox.click()
time.sleep(2)
checkbox.click()
time.sleep(5)
browser.close()
