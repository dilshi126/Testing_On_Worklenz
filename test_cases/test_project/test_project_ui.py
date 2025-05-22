from utilities.ReadConfigurations import ReadConfig

from page_objects.projects.projects_ui import Projects

class TestProjects:
    baseURL = ReadConfig.get_application_url()

    def test_verify_project_ui_elements(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        pu = Projects(self.driver)
        pu.verify_project_ui_elements()
        self.driver.quit()