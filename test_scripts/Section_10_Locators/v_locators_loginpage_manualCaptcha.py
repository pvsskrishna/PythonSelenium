import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#url = r"https://apaims2.0.vassarlabs.com/login"
url = r"https://apaims2.0.vassarlabs.com/schemes/polam-badi"


# chrome
service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(10)
title = driver.title
print(title)
print(driver.current_url)
time.sleep(2)

# Enter username and password
driver.find_element(By.ID, "username").send_keys("mao_4887")
driver.find_element(By.ID, "password").send_keys("Apaims@123")

# Display captcha on screen
captcha_img = driver.find_element(By.ID, "captchaId")
captcha_img.screenshot(r"..\Screenshots\captcha_display.png")
print("Captcha image saved as captcha_display.png — open it and read the captcha.")

# Ask user to manually type captcha
captcha_value = input("Enter the captcha as seen in the image: ")
time.sleep(2)

# Enter captcha and submit
driver.find_element(By.ID, "captcha").send_keys(captcha_value)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)

#clicking schemes
print("clicking")
schemes_button = (By.XPATH,"//a[.//span[normalize-space(text())='Schemes']]")

schemes = WebDriverWait(driver, 15).until(
EC.element_to_be_clickable(schemes_button))

#schemes.click()
driver.execute_script("arguments[0].scrollIntoView(true);", schemes)
time.sleep(1)

try:
    schemes.click()
    print("Clicked Schemes with normal click.")

except:
    # Fallback to JS click
    driver.execute_script("arguments[0].click();", schemes)
    print("Clicked Schemes with JS click.")

WebDriverWait(driver, 15).until(
    EC.url_contains("/schemes"))
print("Schemes page loaded:", driver.current_url)


