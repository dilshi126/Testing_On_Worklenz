from utilities.ReadConfigurations import ReadConfig

from page_objects.projects.project_search_functionality import Projects

class TestProjects:
    baseURL = ReadConfig.get_application_url()

    def test_search_by_name(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        pu = Projects(self.driver)
        pu.search_by_name()
        self.driver.quit()

    def test_search_from_favourite(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        pu = Projects(self.driver)
        pu.search_from_favourite()
        self.driver.quit()

    def test_search_from_archive(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        pu = Projects(self.driver)
        pu.search_from_archive()
        self.driver.quit()