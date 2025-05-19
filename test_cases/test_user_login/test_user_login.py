from utilities.ReadConfigurations import ReadConfig

from page_objects.user_login.user_login import ValidUserLogin


class TestValidLogin:
    baseURL = ReadConfig.get_application_url()

    def test_login_to_account(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.ul = ValidUserLogin(self.driver)
        self.ul.login_to_account()




# python -m pytest test_cases/test_user_login/test_user_login.py
