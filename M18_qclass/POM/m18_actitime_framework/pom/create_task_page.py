class CreateTaskPage:
    def __init__(self, driver):
        self.driver = driver
    def customer_name(self, data):
        self.driver.find_element("name", "customerName").send_keys(data)
    def project_name(self, data):
        self.driver.find_element("name", "projectName").send_keys(data)
    def task_name(self, data):
        self.driver.find_element("name", "task[0].name").send_keys(data)
    def estimate(self, data):
        self.driver.find_element("name", "task[0].budgetedTimeStr").send_keys(data)
    def create_task(self):
        self.driver.find_element("xpath", "//input[@value='Create Tasks']").click()
        results = self.driver.window_handles
        self.driver.switch_to.window(results[0])
    def enter_estimate(self, data):
        self.driver.find_element("xpath", "(//input[@type='text'])[4]").send_keys(data)
    def save_changes(self):
        self.driver.find_element("xpath", "//input[@value='Save Changes']").click()
    def created_task_name(self):
        return self.driver.find_element("xpath", "//a[@title='Click to view task']").text.strip()














