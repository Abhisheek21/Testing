from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(r"C:\Users\abhis\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.presence_of_element_located((By.NAME, "dropdown")))

dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Drop Down Item 4")

time.sleep(3)
driver.quit()
