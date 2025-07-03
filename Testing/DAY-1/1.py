from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = Service(r"C:\Users\abhis\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.google.com/")
search = driver.find_element(By.NAME, "q")
search.send_keys("Amazon")
search.submit()
 
