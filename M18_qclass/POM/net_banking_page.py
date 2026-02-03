class NetBankingPage:
    def __init__(self, driver):
        self.driver = driver
    def user_id(self, data):
        self.driver.find_element("id", "user-id").send_keys(data)
    def password(self, data):
        self.driver.find_element("id", "password").send_keys(data)
    def login(self):
        self.driver.find_element("xpath", "//button[text()='Login']").click()

