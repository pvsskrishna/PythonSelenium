class HomePage:
    def __init__(self, driver):
        self.driver = driver
    def logout(self):
        self.driver.find_element("id", "logoutLink").click()
    def user_tab(self):
        self.driver.find_element("xpath", "//div[text()='Users']").click()
    def select_user(self, username):    #'ln fn (un)'
        self.driver.find_element("xpath", "//img[@id='ext-gen7']").click()
        self.driver.find_element("xpath", f"//div[text()='{username}']").click()
    def new_link(self):
        self.driver.find_element("xpath", "//a[text()='New']").click()
        results = self.driver.window_handles
        self.driver.switch_to.window(results[1])
    







