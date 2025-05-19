import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_locators.locators import LoginPageLocators

app = LoginPageLocators


class ResetPasswordUI :
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def verify_reset_password_UI_elements(self):
        wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()
        try:
            wait.until(EC.presence_of_element_located(app.forgot_password_email))
            wait.until(EC.presence_of_element_located(app.reset_password_button_xpath))
            wait.until(EC.presence_of_element_located(app.return_to_login_button_xpath))

        except NoSuchElementException:
            pytest.fail("Test case is failed")



    def check_reset_password_placeholder_text(self):
        wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.element_to_be_clickable(app.forgot_password_link_xpath)).click()
        time.sleep(2)
        email_input = wait.until(EC.presence_of_element_located(app.forgot_password_email))
        assert email_input.get_attribute("placeholder") == "Enter your email", "Email placeholder text is incorrect"
        print("Placeholder text is correct")


#python -m pytest test_cases/test_reset_password/test_reset_password_ui.py