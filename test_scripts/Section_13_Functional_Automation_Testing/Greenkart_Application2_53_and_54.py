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
names_of_filteredProducts = []
for product in filteredProducts:
    names_of_filteredProducts.append(product.find_element(By.XPATH,"h4").text)
    product.find_element(By.XPATH,"div/button").click()
    t.sleep(0)

cartCount = driver.find_element(By.XPATH,"//div/header/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/strong").text
print(int(cartCount))

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH,"//div/button[@class='promoBtn']").click()
message = driver.find_element(By.CLASS_NAME,"promoInfo")

wait = WebDriverWait(driver,20)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))

print(message.text)
assert message.text == 'Code applied ..!' #Code applied ..!  Invalid code ..!
t.sleep(2)

#TODO: Goal is to sum up the numerical data in total column and validate with the total displaying in checkout page
cost_of_items = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p") #used child concept from css selector
# if we want to write it in XPATH then we can use this: "//tr/td[5]/p"

total = 0
for cost in cost_of_items:
    total += int(cost.text)
print(f"cost total:{total}")

total_displaying = int(driver.find_element(By.CLASS_NAME,"totAmt").text)
print(f"total displaying: {total_displaying}")

assert total == int(total_displaying)

#TODO:1 Validating total:: Total > greater than the total discount displaying.
discount_amount = int(float(driver.find_element(By.CLASS_NAME,"discountAmt").text)) #converting string to float and float to integer. because int("349.2") ❌ error, string not valid for int()
assert discount_amount < total_displaying

#TODO:2 Validating the item names added to the cart and comparing with the list of item names extracted before adding into the cart.
items = []
items_names = driver.find_elements(By.CSS_SELECTOR,"tbody td:nth-child(2) p")
for item in items_names:
    items.append(item.text)
print(f"list of items added to cart:{items}")
print(f"names_of_filteredProducts:{names_of_filteredProducts}")

for name in names_of_filteredProducts:
    assert name in items

