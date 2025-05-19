from utilities.ReadConfigurations import ReadConfig

from page_objects.home.home_ui import HomePageUI
from page_objects.home.create_project_drawer import CreateProjectDrawer


class TestLoginUI:
    baseURL = ReadConfig.get_application_url()


    def test_verify_home_ui(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        hu = HomePageUI(self.driver)
        hu.verify_home_ui()
        self.driver.quit()

    def test_tooltips_on_home_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        hu = HomePageUI(self.driver)
        hu.tooltips_on_home_page()
        self.driver.quit()

