from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

service_obj = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
url = r"https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT,"Shop").click()
products = driver.find_elements(By.XPATH,"//div[@class = 'card h-100']")
totalItemsAddedToCart= 0
for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button[@class='btn btn-info']").click()
        totalItemsAddedToCart += 1
        break
print(f"totalItemsAddedToCart: {totalItemsAddedToCart}")

checkout = driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").text
checkedOutItemsCount = int(checkout.split("(")[1].split(")")[0].strip())
print(f"checkedOutItemsCount: {checkedOutItemsCount}")
assert totalItemsAddedToCart == checkedOutItemsCount

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class = 'btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
success_message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(success_message)

assert "Success! Thank you!" in success_message
time.sleep(2)
driver.close()
