"""
Day 19

assignment:
-----------
ws to launch https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand&gclsrc=aw.ds&gad_source=1&gad_campaignid=19863995494&gbraid=0AAAAADLp3cEygg3qqw3KWN4HIBioCYA2e&gclid=Cj0KCQiAvOjKBhC9ARIsAFvz5lguz00zGqk13g89vp5afVI5YcUzCKh0x2PJ4vdFcMR8uaiJfCVUnoQaAq6tEALw_wcB
create 5 different naukri profile, read data from excel file.
"""
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import ChromiumOptions
o = ChromiumOptions()
o.add_experimental_option("detach", False)
o.add_argument("--disable-notifications")

driver = Chrome(options = o)
wait = WebDriverWait(driver,10)

def takeScreenshot():
    screenshotName = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    driver.get_screenshot_as_file(f"./screenshots_test/{screenshotName}.png")

def exceldata():
    workbook = openpyxl.load_workbook(r"./datasets_excels/data.xlsx")
    sheet = workbook["Sheet2"]

    headers = [cell.value for cell in sheet[1] if cell.value is not None]
    print(f"headers:{headers}") #['fullName','emaiID','password','mobileNo','workStatus']

    data = list(sheet.iter_rows(min_row=2,max_col=len(headers),values_only=True))
    print(f"data:  {data}")

    return data

def testCase1():
    try:
        data = exceldata()
        for fullName,emaiID,password,mobileNo,workStatus in data:
            driver.get(r"https://www.naukri.com/registration/createAccount")
            driver.maximize_window()

            driver.find_element(By.XPATH,"//input[@id='name']").send_keys(fullName) #fullName
            driver.find_element(By.XPATH,"//input[@id='email']").send_keys(emaiID) #emaiID
            driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password) #password
            driver.find_element(By.XPATH,"//input[@id='mobile']").send_keys(mobileNo) #mobileNo

            if workStatus == 'yes':
                driver.find_element(By.XPATH,"//div[@data-val='exp']").send_keys(workStatus) #workStatus
            else:
                driver.find_element(By.XPATH, "//div[@data-val='fresher']").send_keys(workStatus)  # workStatus

            driver.find_element(By.XPATH,"//span[text()='Send me important updates & promotions via SMS, email, and']").click() #checkBox
            driver.find_element(By.XPATH,"//button[.='Register now']").click() #registerBtn

    except Exception as e:
        takeScreenshot()
        print(f"error is: {e}")
        raise
    finally:
        driver.close()

exceldata()
testCase1()