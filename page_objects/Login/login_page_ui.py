import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_locators.locators import LoginPageLocators

app = LoginPageLocators


class LoginUI :
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def verify_UI_elements(self):

        try:
            self.wait.until(EC.presence_of_element_located(app.login_email_id))
            self.wait.until(EC.presence_of_element_located(app.login_password_id))
            self.wait.until(EC.presence_of_element_located(app.remember_me_id))
            self.wait.until(EC.presence_of_element_located(app.forgot_password_link_xpath))
            self.wait.until(EC.presence_of_element_located(app.login_button_css))
            self.wait.until(EC.presence_of_element_located(app.signin_with_google_xpath))
            self.wait.until(EC.presence_of_element_located(app.signup_link_xpath))
            print("Test case is passed")
        except NoSuchElementException:
            pytest.fail("Test case is failed")



    def check_placeholder_text(self):
        email_input = self.wait.until(EC.presence_of_element_located(app.login_email_id))
        password_input = self.wait.until(EC.presence_of_element_located(app.login_password_id))

        assert email_input.get_attribute("placeholder") == "Enter your email", "Email placeholder text is incorrect"
        assert password_input.get_attribute("placeholder") == "Enter your password", "Password placeholder text is incorrect"
        print("Placeholder text is correct")
