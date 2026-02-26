import pytest

# def test_case1(a,b):
#     print(a+b)
#     print("no parameter marker")
#
# test_case1(1,2)

@pytest.mark.parametrize("a",[10,20,30])
def test_case1(a):
    print(f"input value a: {a}")

@pytest.mark.parametrize("a,b",[(10,20),(1,2)])
def test_add1(a,b):
    print(f"a + b: {a+b}")

@pytest.mark.parametrize("a,b,c", [[10, 20, 5]])
def test_add2(a, b, c):
    print(f"a + b + c: {a + b + c}")

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import ChromiumOptions
import time
from selenium.webdriver.common.keys import Keys
options = ChromiumOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")

@pytest.fixture
def driver():
    driver = Chrome(options=options)
    yield driver
    driver.quit()

# driver = Chrome(options=options)
driver.implicitly_wait(20)

@pytest.mark.parametrize("relation,gender,email, mobile, pwd",(
        ["Self",'Male',"self123334@gmail.com","9222222222","self123334@gmail.com"],
        ["Son",'Female',"self123334@gmail.com","9222222222","self123334@gmail.com"],
        ["Daughter",'Male',"self123335@gmail.com","9333333333","self123335@gmail.com"],
        ["Brother",'Male',"self123336@gmail.com","9444444444","self123336@gmail.com"]))
def test_register(driver,relation,gender,email, mobile, pwd):
    driver.get(r"https://www.jeevansathi.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"relationshipBlock").click()
    driver.find_element(By.XPATH,f"//div/ul/li[text()='{relation}']").click()
    if relation == "Self":
        driver.find_element(By.ID,"gender").click()
        driver.find_element(By.XPATH,f"//div/ul/li[text()='{gender}']").click()
    driver.find_element(By.ID,"email").send_keys(f"{email}")
    driver.find_element(By.ID,"phoneNumber").send_keys(f"{mobile}")
    driver.find_element(By.ID,"password").send_keys(f"{pwd}")
    driver.find_element(By.ID,"register_button").click()
    time.sleep(2)
    driver.quit()

@pytest.mark.parametrize("product",["wedding gift", "baby", "book lover gifts", "host gift"])
def test_etsy(driver,product):
    driver.get(r"https://www.etsy.com/in-en/?ref=lgo")
    driver.maximize_window()
    driver.find_element(By.ID,"global-enhancements-search-query").send_keys(product + Keys.ENTER)
    items = driver.find_elements(By.XPATH,"//h3[contains(@id, 'listing-title')]")
    for item in items:
        print(item.text)
    time.sleep(5)
    driver.quit()

