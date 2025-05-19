import time
from wsgiref.validate import assert_

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data.test_data import LoginCredentials
from test_locators.locators import LoginPageLocators

app = LoginPageLocators
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def perform_login(self, username, password):
        self.wait.until(EC.presence_of_element_located(app.login_email_id)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(app.login_password_id)).send_keys(password)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(app.login_button_css)).click()



    def verify_login_with_valid_credentials(self):
        self.perform_login(LoginCredentials.valid_email, LoginCredentials.valid_password)
        try:
            self.wait.until(
                EC.visibility_of_element_located((app.create_project_xpath)))
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Login failed")



    def verify_signup_link(self):
        self.wait.until(EC.visibility_of_element_located(app.signup_link_xpath)).click()
        try:
            self.wait.until(EC.visibility_of_element_located(app.signup_name_id))
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Test case failed")



    def verify_login_with_invalid_email_format(self):
        self.perform_login (LoginCredentials.invalid_email_format,LoginCredentials.valid_password)
        try:
            self.wait.until(EC.presence_of_element_located(app.email_error_notify_xpath))
            print("Test case passed")

        except NoSuchElementException:
            pytest.fail("Login failed")




    def verify_login_with_invalid_email(self):
        self.perform_login(LoginCredentials.invalid_email,LoginCredentials.valid_password)
        self.error_notification()



    def verify_login_with_invalid_password(self):
        self.perform_login(LoginCredentials.valid_email,LoginCredentials.invalid_password)
        self.error_notification()



    def error_notification(self):
        try:
            self.wait.until(EC.presence_of_element_located(app.empty_error_notify_xpath))
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Login failed")




    def verify_login_with_empty_field(self):
        self.perform_login(LoginCredentials.empty_email,LoginCredentials.empty_password)

        try:
            self.wait.until(EC.visibility_of_element_located(app.login_button_css))
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Login failed")


    def password_masking(self):
        password_field = self.wait.until(EC.presence_of_element_located(app.login_password_id))
        field_type = password_field.get_attribute("type")

        assert field_type == "password", f"Password field is not masked! Found type: {field_type}"
        print("Password field is properly masked as 'password'")

    def toggle_password_visibility(self):
        password_field = self.wait.until(EC.presence_of_element_located(app.login_password_id))
        password_field.send_keys(LoginCredentials.valid_password)
        initial_type = password_field.get_attribute("type")
        assert initial_type == "password", f"Expected password field to be masked initially. Found type: {initial_type}"

        eye_icon = self.wait.until(EC.element_to_be_clickable(app.eye_icon_xpath))
        eye_icon.click()
        time.sleep(1)

        password_field = self.wait.until(EC.presence_of_element_located(app.login_password_id))
        visible_type = password_field.get_attribute("type")
        assert visible_type == "text", f"Expected password field to be visible after clicking eye icon. Found type: {visible_type}"

        eye_icon = self.wait.until(EC.element_to_be_clickable(app.eye_icon_xpath))
        eye_icon.click()
        time.sleep(1)

        password_field = self.wait.until(EC.presence_of_element_located(app.login_password_id))
        final_type = password_field.get_attribute("type")
        assert final_type == "password", f"Expected password field to be masked again. Found type: {final_type}"

        print("Test passed")
