from utilities.ReadConfigurations import ReadConfig

from page_objects.home.import_template import ImportTemp

class TestImportTemp:
    baseURL = ReadConfig.get_application_url()

    # def test_open_select_from_template_drawer(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     otd = ImportTemp(self.driver)
    #     otd.open_select_from_template_drawer()
    #     self.driver.quit()

    def test_create_project_by_importing_template(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        pit = ImportTemp(self.driver)
        pit.create_project_by_importing_template()
        self.driver.quit()