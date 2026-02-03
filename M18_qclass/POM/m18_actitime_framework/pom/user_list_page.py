class UserListPage:
    def __init__(self, driver):
        self.driver = driver
    def user_button(self):
        self.driver.find_element("xpath", "//span[text()='User']").click()
    def first_name(self, data):
        self.driver.find_element("name", "firstName").send_keys(data)
    def last_name(self, data):
        self.driver.find_element("name", "lastName").send_keys(data)
    def email(self, data):
        self.driver.find_element("name", "email").send_keys(data)
    def username(self, data):
        self.driver.find_element("name", "username").send_keys(data)
    def password(self, data):
        self.driver.find_element("name", "password").send_keys(data)
    def retype_password(self, data):
        self.driver.find_element("name", "passwordCopy").send_keys(data)
    def create_user(self):
        self.driver.find_element("xpath", "//div[text()='Create User']").click()
    def create_new_user_popup(self):
        return self.driver.find_element("xpath", "//span[@id='userDataLightBox_titlePlaceholder']").text
    def created_username(self):
        return self.driver.find_element("xpath", "//div[@class='name']").text









