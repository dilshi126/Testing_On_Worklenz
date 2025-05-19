from utilities.ReadConfigurations import ReadConfig

from page_objects.home.create_project_drawer import CreateProjectDrawer

class TestCreateProject:
    baseURL = ReadConfig.get_application_url()


    # def test_verify_open_create_project_drawer(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     cp = CreateProjectDrawer(self.driver)
    #     cp.verify_open_create_project_drawer()
    #     self.driver.quit()
    #
    # def test_verify_project_drawer_ui(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     cp = CreateProjectDrawer(self.driver)
    #     cp.verify_project_drawer_ui()
    # #     self.driver.quit()

    def test_creating_new_project(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        cp = CreateProjectDrawer(self.driver)
        cp.creating_new_project()
        self.driver.quit()

