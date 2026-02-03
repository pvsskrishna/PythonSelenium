from time import sleep
import pytest

from welcome_page import *
from savings_account_page import *
from sb_account_open_page import *

@pytest.mark.skip(reason="loading issue")
def test_testcase1(launch):
    driver = launch
    w = WelcomePage(driver)
    w.accounts()
    s = SavingsAccountPage(driver)
    s.apply()
    sb = SBAccountOpenPage(driver)
    sb.full_name("akash")
    sb.pan("LCHPS1234H")
    sb.mobile_number("9988776655")
    sb.otp("987654")
    sb.pincode("560010")
    sb.tc_checkbox()
    sleep(5)
    sb.apply_now()

