from utilities.ReadConfigurations import ReadConfig

from page_objects.project_inside.project_ui import ProjectInside

class TestProjects:
    baseURL = ReadConfig.get_application_url()

    def test_verify_project_inside_ui(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        pu = ProjectInside(self.driver)
        pu.verify_project_inside_ui()
        self.driver.quit()