from utilities.ReadConfigurations import ReadConfig

from page_objects.home.task_table import TaskTable

class TestTaskTable:
    baseURL = ReadConfig.get_application_url()

    def test_visibility_of_add_a_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        otd = TaskTable(self.driver)
        otd.visibility_of_add_a_task()
        self.driver.quit()

