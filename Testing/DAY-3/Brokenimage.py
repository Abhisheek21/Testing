import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up ChromeDriver path
service = Service(r"C:\Users\abhis\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service)

# Open the target webpage
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

# Get all <img> elements
images = browser.find_elements(By.TAG_NAME, "img")

# Check for broken images
broken_images = []
for image in images:
    src = image.get_attribute("src")
    if src:
        try:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print(f"Broken image found: {src}")
        except Exception as e:
            broken_images.append(src)
            print(f"Error checking image: {src} — {e}")

# Display results
if broken_images:
    print("\nList of broken images:")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No broken images found.")

# Close the browser
browser.quit()
