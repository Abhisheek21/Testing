from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, os

screenshot_path = r"C:\Users\abhis\OneDrive\Desktop\Testing\Screenshot"
os.makedirs(screenshot_path, exist_ok=True)

Cdriver.maximize_window()

driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Flipkart")
driver.find_element(By.NAME, "q").submit()
time.sleep(2)

driver.get("https://www.flipkart.com")
time.sleep(2)

try:
    driver.find_element(By.XPATH, "//button[contains(text(), '✕')]").click()
except NoSuchElementException:
    pass

driver.find_element(By.NAME, "q").send_keys("iphone 16 pro max")
time.sleep(2)

try:
    suggestions = driver.find_elements(By.XPATH, "//ul[contains(@class, '_1sFryS')]/li")
    assert suggestions, "Assertion failed: No suggestions found."
    suggestions[0].click()
    time.sleep(2)
    assert os.path.exists(screenshot_path), "Screenshot directory missing!"
    driver.save_screenshot(os.path.join(screenshot_path, "suggestion_clicked.png"))

    products = driver.find_elements(By.XPATH, "//div[@data-id]")
    assert products, "Assertion failed: No products found after clicking suggestion."
    driver.save_screenshot(os.path.join(screenshot_path, "product_found.png"))

    driver.execute_script("alert('Assertion passed: Product found.');")
    print("Assertion passed: Product found.")

except AssertionError as ae:
    driver.save_screenshot(os.path.join(screenshot_path, "assertion_failure.png"))
    driver.execute_script(f"alert('{ae}');")
except Exception as e:
    driver.save_screenshot(os.path.join(screenshot_path, "unexpected_error.png"))
    driver.execute_script(f"alert('Unexpected error: {e}');")
finally:
    time.sleep(2)
    driver.quit()
