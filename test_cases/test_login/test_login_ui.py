from utilities.ReadConfigurations import ReadConfig

from page_objects.Login.login_page_ui import LoginUI


class TestLoginUI:
    baseURL = ReadConfig.get_application_url()

    def test_verify_UI_elements(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lu = LoginUI(self.driver)
        self.lu.verify_UI_elements()
        self.driver.quit()


    def test_check_placeholder_text(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lu = LoginUI(self.driver)
        self.lu.check_placeholder_text()
        self.driver.quit()

