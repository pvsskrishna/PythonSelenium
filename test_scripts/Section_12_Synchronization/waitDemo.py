from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time as t

service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

url = r"https://rahulshettyacademy.com/seleniumPractise/#/"
driver.get(url)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys('ber')

t.sleep(2)
filteredProducts = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(filteredProducts)
assert count > 0
for product in filteredProducts:
    product.find_element(By.XPATH,"div/button").click()
    t.sleep(0)

cartCount = driver.find_element(By.XPATH,"//div/header/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/strong").text
print(int(cartCount))

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH,"//div/button[@class='promoBtn']").click()
message = driver.find_element(By.CLASS_NAME,"promoInfo").text
print(message)
assert message == 'Code applied ..!' #Code applied ..!  Invalid code ..!
t.sleep(2)























'''search_button = driver.find_element(By.CLASS_NAME,"search-button")
search_button.click()
products = driver.find_elements(By.XPATH,"//div[@class = 'product']/h4")
pnames =[]
for product in products:
    pname = (product.text.split('-'))[0]
    pnames.append(pname[:len(pname)-1])
print(pnames)

for _ in pnames:
    print(_)

t.sleep(2)'''