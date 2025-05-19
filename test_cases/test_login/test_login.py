from utilities.ReadConfigurations import ReadConfig

from page_objects.Login.login_page import LoginPage


class TestLogin:
    baseURL = ReadConfig.get_application_url()

    def test_verify_login_with_valid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.verify_login_with_valid_credentials()
        self.driver.quit()

    def test_verify_signup_link(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.verify_signup_link()
        self.driver.quit()

    def test_verify_login_with_invalid_email_format(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.verify_login_with_invalid_email_format()
        self.driver.quit()

    def test_verify_login_with_invalid_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.verify_login_with_invalid_email()
        self.driver.quit()

    def test_verify_login_with_invalid_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.verify_login_with_invalid_password()
        self.driver.quit()

    def test_verify_login_with_empty_field(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.verify_login_with_empty_field()
        self.driver.quit()

    def test_password_masking(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.password_masking()
        self.driver.quit()

    def test_toggle_password_visibility(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = LoginPage(self.driver)
        self.lg.toggle_password_visibility()
        self.driver.quit()