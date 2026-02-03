import pytest
from generic.assertion import text_assertion
from generic.verification import verify_title
from pom.login_page import *
from pom.home_page import *

@pytest.mark.parametrize("un, pwd, reason", [("admin", "admin", "invalid"),
                                     ("admin", "122345", "invalid"),
                                     ("admin", "manager", "valid")])
def test_testcase1(launch, un, pwd, reason):
    driver = launch
    verify_title('actiTIME - Login',driver)
    l = LoginPage(driver)
    l.username(un)
    l.password(pwd)
    l.login()
    if reason == "invalid":
        error_msg = l.error_message()
        text_assertion(error_msg, "Username or Password is invalid. Please try again.", driver)
    else:
        verify_title('actiTIME - Enter Time-Track',driver)
        h = HomePage(driver)
        h.logout()
        verify_title('actiTIME - Login', driver)


