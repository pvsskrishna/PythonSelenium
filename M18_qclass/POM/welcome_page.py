from time import sleep

class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
    def accounts(self):
        self.driver.find_element("xpath", "//span[text()=' Accounts ']").click()
    def loans(self):
        self.driver.find_element("xpath", "//span[text()=' Loans ']").click()
    def higher_education_checkbox(self):
        self.driver.find_element("xpath", "//p[text()='Higher Education']").click()
    def next(self):
        self.driver.find_element("xpath", "//button[text()='NEXT']").click()
    def apply(self):
        sleep(2)
        self.driver.find_element("xpath", "//a[text()='APPLY']").click()
        sleep(3)
        results = self.driver.window_handles
        self.driver.switch_to.window(results[1])
    def deposits(self):
        self.driver.find_element("xpath", "//span[text()=' Deposits ']").click()
    def fixed_deposits(self):
        self.driver.find_element("xpath", "//p[text()='Fixed Deposit']").click()
    def _10L(self):
        self.driver.find_element("xpath", "//label[text()='10 L']").click()
    def on_maturity(self):
        self.driver.find_element("xpath", "//label[text()='On Maturity']").click()
    def senior_citizen(self):
        self.driver.find_element("xpath", "//p[text()='Senior Citizen']").click()
    def open_fd(self):
        self.driver.find_element("xpath", "//a[text()='OPEN FIXED DEPOSIT']").click()
        results = self.driver.window_handles
        self.driver.switch_to.window(results[1])




































