from time import sleep

from welcome_page import *
from education_loan_page import *

def test_testcase2(launch):
    driver = launch
    w = WelcomePage(driver)
    sleep(2)
    w.loans()
    sleep(2)
    w.higher_education_checkbox()
    w.next()
    w.apply()
    e = EducationLoanPage(driver)
    e.first_name("akash")
    e.last_name("kumar")
    e.email("akash123@gmail.com")
    e.mobile("9988776655")
    e.country("India")
    e.pincode("560010")
    e.check_box()
    e.submit()



































