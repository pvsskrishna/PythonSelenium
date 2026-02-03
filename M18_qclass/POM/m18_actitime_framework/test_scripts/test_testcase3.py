from generic.verification import verify_title
from pom.login_page import *
from pom.home_page import *
from pom.create_task_page import *
from generic.assertion import text_assertion

def test_testcase3(launch):
    driver = launch
    verify_title('actiTIME - Login',driver)
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login()
    verify_title('actiTIME - Enter Time-Track',driver)
    h = HomePage(driver)
    h.select_user("automation, selenium (seleniumauto)")
    h.new_link()
    c = CreateTaskPage(driver)
    c.customer_name("ICICI Bank")
    c.project_name("mobile application")
    c.task_name("test scenario and test case")
    c.estimate("9")
    c.create_task()
    etask_name = c.created_task_name()
    text_assertion(etask_name, "test scenario and test case", driver)
    h.logout()
    verify_title('actiTIME - Login', driver)
    l = LoginPage(driver)
    l.username("seleniumauto")
    l.password("selenium@123")
    l.login()
    verify_title('actiTIME - Enter Time-Track', driver)
    c.enter_estimate("9")
    c.save_changes()
    h.logout()
    verify_title('actiTIME - Login', driver)




