from generic.verification import verify_title
from pom.login_page import *
from pom.home_page import *
from pom.user_list_page import *
from generic.assertion import text_assertion
from generic.excel_read import read_data

d = read_data()     #d={'fn':'selenum'}

def test_testcase2(launch):
    driver = launch
    verify_title(d['login_title'],driver)
    l = LoginPage(driver)
    l.username(d['admin_username'])
    l.password(d['admin_pwd'])
    l.login()
    verify_title(d['homepage_title'], driver)
    h = HomePage(driver)
    h.user_tab()
    verify_title(d['userpage_title'], driver)
    u = UserListPage(driver)
    u.user_button()
    etext = u.create_new_user_popup()
    text_assertion(etext, "Create New User", driver)
    u.first_name(d['first_name'])
    u.last_name(d['last_name'])
    u.email(d['email'])
    u.username(d['username'])
    u.password(d['password'])
    u.retype_password(d['retype_pwd'])
    u.create_user()
    eusername = u.created_username()
    text_assertion(eusername, "automation, selenium (seleniumauto)", driver)
    h.logout()
    verify_title(d['login_title'], driver)
    l = LoginPage(driver)
    l.username(d['created_un'])
    l.password(d['created_pwd'])
    l.login()
    verify_title(d['homepage_title'], driver)
    h.logout()
    verify_title(d['login_title'], driver)


#     assignmentsql@gmail.com










