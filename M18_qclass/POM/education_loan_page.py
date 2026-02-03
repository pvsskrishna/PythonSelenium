from selenium.webdriver.support.select import Select

class EducationLoanPage:
    def __init__(self, driver):
        self.driver = driver
    def first_name(self, data):
        self.driver.find_element("name", "first_name").send_keys(data)
    def last_name(self, data):
        self.driver.find_element("name", "last_name").send_keys(data)
    def email(self, data):
        self.driver.find_element("name", "email_personal").send_keys(data)
    def mobile(self, data):
        self.driver.find_element("name", "mobile_personal").send_keys(data)
    def country(self, data):
        country_dd = self.driver.find_element("name", "country")
        s = Select(country_dd)
        s.select_by_visible_text(data)
    def pincode(self, data):
        self.driver.find_element("name", "pincode").send_keys(data)
    def check_box(self):
        self.driver.find_element("xpath", "//div[@class='cmn-checkmark']").click()
    def submit(self):
        self.driver.find_element("id", "cmmon-btn-ctn").click()





