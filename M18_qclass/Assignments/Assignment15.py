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

from openpyxl import *

driver = Chrome(options = o)
wait = WebDriverWait(driver,10)

def takeScreenshot():
    screenshotName = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    driver.get_screenshot_as_file(f"./screenshots_test/{screenshotName}.png")

def exceldata():
    workbook = openpyxl.load_workbook(r"./datasets_excels/data.xlsx")
    sheet = workbook["Sheet2"]
    details = []
    headers = [cell.value for cell in sheet[1]]
    print(f"headers:{headers}") #['fullName','emaiID','password','mobileNo','workStatus']

    row_data = []
    for value in sheet.iter_rows(min_row=2,values_only=True):
        row_data.append(value)

    creds = {}
    for header,value in zip(headers,row_data):
        creds[header] = value
    details.append(creds)
    print(details)






        # fullName = ""
        # emaiID = ""
        # password = ""
        # mobileNo = ""
        # workStatus = ""
        # checkBox = ""
        # registerBtn = ""

# def testCase1():
#     try:
#         driver.get(r"https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium"
#                    r"=cpc&utm_campaign=Brand&gclsrc=aw.ds&gad_source=1&gad_campaignid=19863995494&gbraid=0AAAAADLp3cEygg"
#                    r"3qqw3KWN4HIBioCYA2e&gclid=Cj0KCQiAvOjKBhC9ARIsAFvz5lguz00zGqk13g89vp5afVI5YcUzCKh0x2PJ4vdFcMR8uaiJfCVUnoQaAq6tEALw_wcB")
#         driver.maximize_window()
#         driver.find_element(By.XPATH,"") #fullName
#         driver.find_element(By.XPATH,"") #emaiID
#         driver.find_element(By.XPATH,"") #password
#         driver.find_element(By.XPATH,"") #mobileNo
#         driver.find_element(By.XPATH,"") #workStatus
#         driver.find_element(By.XPATH,"") #checkBox
#         driver.find_element(By.XPATH,"") #registerBtn
#
#     except Exception as e:
#         takeScreenshot()
#         print(f"error is: {e}")
#         raise
#     finally:
#         driver.close()

exceldata()