
#30/12/2025 ---> Day 14
#
# assignment on assert and take screenshot
# launch https://medlineplus.gov/ > click on genetics > click on genetic conditions > click on see Triple A syndrome
# > Autonomic Nervous System Disorders > Find an Expert
#
# C:\Users\varun\PycharmProjects\PythonSelenium\M18_qclass\Assignments\screenshots_test
import time
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import ChromiumOptions
o = ChromiumOptions()
o.add_experimental_option("detach",False)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

SCREENSHOTFOLDERFILEPATH = "screenshots_test"
TIMESTAMP = datetime.now().strftime("%d-%m-%y_%H-%M-%S")

driver = Chrome(options=o)
def testCase1():
    try:
        driver.implicitly_wait(20)
        driver.get(r"https://pharmeasy.in/")
        #driver.maximize_window()
        print("screenshot_name", TIMESTAMP)
        wait = WebDriverWait(driver,10)
        TAKE_SCREENSHORT = driver.get_screenshot_as_file(f"{SCREENSHOTFOLDERFILEPATH}//{TIMESTAMP}.png")
        assert driver.title == "PharmEasy – Online Pharmacy & Medical Store with Healthcare Services in India | 50 Lakhs+ Customers", TAKE_SCREENSHORT
        driver.find_element(By.XPATH,"(//a[.='Medicine'])[2]").click()
        print("clicked on medicine tab")

        assert driver.title == "Buy Medicines Online - Up to 24% OFF | Fast Delivery by PharmEasy", TAKE_SCREENSHORT
        driver.find_element(By.XPATH,"//span[.='Search for Medicines...']").click()
        driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Dolo 650")
        print("Entered medicine name")

        time.sleep(5)
        driver.find_element(By.XPATH,"//div[.='Dolo 650']").click()
        assert driver.title == 'Order DOLO 650 Online - PharmEasy', TAKE_SCREENSHORT
        print('Medicine searched and selected')

        driver.find_element(By.XPATH,"(//button[.='Add To Cart'])[1]").click()
        print("Clicked on add to cart")

        driver.find_element(By.XPATH,"(//li[@data-value='1'])").click()
        driver.find_element(By.XPATH,"//button[.='View Cart']").click()
        print('Clicked on view cart button')

        time.sleep(5)
        assert driver.title == "Order Medicines Online - Cart - PharmEasy", TAKE_SCREENSHORT
        driver.find_element(By.XPATH,"//span[.='Add Delivery Address']").click()
        print("clicked on add delivery address button")

        driver.find_element(By.ID,"mobile").send_keys("9988998899")
        driver.find_element(By.XPATH,"//button[.='Send OTP']")
        print("clicked on send otp")

    except Exception as e:
        driver.get_screenshot_as_file(f"{SCREENSHOTFOLDERFILEPATH}//{TIMESTAMP}.png")
        print(f"testCase1 Error is: {e}")

def testCase2():
    try:
        driver.get(r"https://medlineplus.gov/")
        TAKE_SCREENSHORT = driver.get_screenshot_as_file(f"{SCREENSHOTFOLDERFILEPATH}//{TIMESTAMP}.png")
        assert driver.title == "MedlinePlus - Health Information from the National Library of Medicine", TAKE_SCREENSHORT
        driver.find_element(By.XPATH,"(//a[.='Genetics'])[2]").click()
        print("clicked on genitics")

        assert driver.title == "MedlinePlus: Genetics", TAKE_SCREENSHORT
        driver.find_element(By.XPATH,"//h2[.='Genetic Conditions']").click()
        print("clicked on Genetic conditions")

        assert driver.title == "MedlinePlus: Genetic Conditions", TAKE_SCREENSHORT
        driver.find_element(By.XPATH, "(//a[.='Triple A syndrome'])[1]").click()
        print("clicked on Triple A syndrome")

        assert driver.title == "Triple A syndrome: MedlinePlus Genetics", TAKE_SCREENSHORT
        driver.find_element(By.XPATH, "//a[.='Autonomic Nervous System Disorders']").click()
        print("clicked on Autonomic Nervous System Disorders")

        assert driver.title == "Dysautonomia | Autonomic Nervous System Disorders | MedlinePlus", TAKE_SCREENSHORT
        driver.find_element(By.XPATH, "//a[.='Find an Expert']").click()
        print("clicked on Find an Expert")

    except Exception as e:
        driver.get_screenshot_as_file(f"{SCREENSHOTFOLDERFILEPATH}//{TIMESTAMP}.png")
        print(f" testCase2 Error is: {e}")