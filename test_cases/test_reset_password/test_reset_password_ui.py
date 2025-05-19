from utilities.ReadConfigurations import ReadConfig

from page_objects.forgot_password.reset_pasword_ui import ResetPasswordUI


class TestResetPasswordUI:
    baseURL = ReadConfig.get_application_url()

    def test_verify_reset_password_UI_elements(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPasswordUI(self.driver)
        self.rp.verify_reset_password_UI_elements()
        self.driver.quit()


    def test_check_reset_password_placeholder_text(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPasswordUI(self.driver)
        self.rp.check_reset_password_placeholder_text()
        self.driver.quit()

