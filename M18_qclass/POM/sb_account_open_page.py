class SBAccountOpenPage:
    def __init__(self, driver):
        self.driver = driver
    def full_name(self, data):
        self.driver.find_element("id", "name").send_keys(data)
    def pan(self, data):
        self.driver.find_element("id", "pan").send_keys(data)
    def pincode(self, data):
        self.driver.find_element("id", "pincode").send_keys(data)
    def mobile_number(self, data):
        self.driver.find_element("id", "mobile_number").send_keys(data)
    def otp(self, data):
        self.driver.find_element("id", "otp").send_keys(data)
    def tc_checkbox(self):
        self.driver.find_element("id", "checkbox").click()
    def apply_now(self):
        self.driver.find_element("xpath", "//button[text()='Apply Now']").click()
