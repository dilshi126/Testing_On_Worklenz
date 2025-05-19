import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data.test_data import LoginCredentials
from test_locators.locators import LoginPageLocators

app = LoginPageLocators
class ResetPassword:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)



    def forget_password(self):
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()

        try:
            self.wait.until(EC.presence_of_element_located(app.reset_password_button_xpath))
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Test case failed")


    def return_login_button(self):
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(app.return_to_login_button_xpath)).click()
        time.sleep(2)
        self.display_login_button()


    def display_login_button(self):
        try:
            login_btn = self.wait.until(EC.presence_of_element_located(app.login_button_css))
            assert login_btn.is_displayed()
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Test case failed")


    def verify_reset_password_with_invalid_email(self):
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()
        self.wait.until(EC.presence_of_element_located(app.forgot_password_email)).send_keys(LoginCredentials.invalid_email)
        self.wait.until(EC.element_to_be_clickable(app.reset_password_button_xpath)).click()
        time.sleep(2)
        self.error_message()



    def reset_password_with_unregistered_email(self):
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()
        self.wait.until(EC.presence_of_element_located(app.forgot_password_email)).send_keys(LoginCredentials.unregistered_email)
        self.wait.until(EC.element_to_be_clickable(app.reset_password_button_xpath)).click()
        time.sleep(2)
        self.error_message()



    def error_message_for_empty_input_field(self):
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()
        self.wait.until(EC.presence_of_element_located(app.forgot_password_email))
        self.wait.until(EC.element_to_be_clickable(app.reset_password_button_xpath)).click()
        time.sleep(2)
        try:
            self.wait.until(EC.presence_of_element_located(app.email_empty_notification))
            print("Test case passed")

        except NoSuchElementException:
            pytest.fail("Test case failed")



    def error_message(self):
        try:
            self.wait.until(EC.presence_of_element_located(app.account_does_not_exist_error))
            print("Test case passed")

        except NoSuchElementException:
            pytest.fail("Test case failed")


#python -m pytest test_cases/test_reset_password/test_reset_password.py
