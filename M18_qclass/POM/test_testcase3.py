from welcome_page import *
from net_banking_page import *

def test_testcase3(launch):
    driver = launch
    w = WelcomePage(driver)
    sleep(3)
    w.deposits()
    w.fixed_deposits()
    w._10L()
    w.on_maturity()
    w.senior_citizen()
    w.next()
    w.open_fd()
    n = NetBankingPage(driver)
    sleep(3)
    n.user_id("selenium1234")
    n.password("ABCD1234@!##gghf")
    n.login()










