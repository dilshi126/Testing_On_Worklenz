import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data.test_data import LoginCredentials
from test_locators.locators import LoginPageLocators
from test_data.test_data import LoginCredentials

app = LoginPageLocators
data=LoginCredentials

class ValidUserLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def valid_user_email(self):
        self.wait.until(EC.presence_of_element_located(app.login_email_id)).send_keys(data.valid_email)

    def valid_user_password(self):
        self.wait.until(EC.presence_of_element_located(app.login_password_id)).send_keys(data.valid_password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(app.login_button_css)).click()

    def login_to_account(self):
        self.valid_user_email()
        self.valid_user_password()
        time.sleep(2)
        self.click_login_button()

