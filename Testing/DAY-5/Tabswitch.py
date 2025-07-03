from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("First Tab Title:", driver.title)

driver.execute_script("window.open('https://www.bing.com');")
time.sleep(2)

tabs = driver.window_handles

driver.switch_to.window(tabs[1])
print("Second Tab Title:", driver.title)

driver.switch_to.window(tabs[0])
print("Switched Back to:", driver.title)
