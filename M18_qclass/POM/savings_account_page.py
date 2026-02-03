class SavingsAccountPage:
    def __init__(self, driver):
        self.driver = driver
    def apply(self):
        self.driver.find_element("xpath", "(//a[contains(text(), 'APPLY*')])[2]").click()
        results = self.driver.window_handles
        self.driver.switch_to.window(results[1])
