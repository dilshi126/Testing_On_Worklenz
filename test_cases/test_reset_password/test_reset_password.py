from utilities.ReadConfigurations import ReadConfig

from page_objects.forgot_password.reset_password import ResetPassword


class TestResetPassword:
    baseURL = ReadConfig.get_application_url()

    def test_forget_password(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPassword(self.driver)
        self.rp.forget_password()
        self.driver.quit()


    def test_return_login_button(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPassword(self.driver)
        self.rp.return_login_button()
        self.driver.quit()

    def test_verify_reset_password_with_invalid_email(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPassword(self.driver)
        self.rp.verify_reset_password_with_invalid_email()
        self.driver.quit()

    def test_reset_password_with_unregistered_email(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPassword(self.driver)
        self.rp.reset_password_with_unregistered_email()
        self.driver.quit()


    def test_error_message_for_empty_input_field(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = ResetPassword(self.driver)
        self.rp.error_message_for_empty_input_field()
        self.driver.quit()