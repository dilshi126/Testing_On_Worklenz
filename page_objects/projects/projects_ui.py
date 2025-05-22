import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_cases.conftest import setup
from test_cases.test_user_login.test_user_login import TestValidLogin
from test_locators.locators import ProjectUI

project=ProjectUI

class Projects:
    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login_credentials(self):
        login = TestValidLogin()
        login.test_login_to_project_account(self.driver)
        time.sleep(5)

    def verify_project_ui_elements(self):
        self.login_credentials()
        self.wait.until(EC.presence_of_element_located(project.project_tab_css)).click()
        try:
            self.wait.until(EC.presence_of_element_located(project.all_tab_css))
            self.wait.until(EC.presence_of_element_located(project.favourite_tab_css))
            self.wait.until(EC.presence_of_element_located(project.archive_tab_css))
            self.wait.until(EC.presence_of_element_located(project.favourite_icon_css))
            self.wait.until(EC.presence_of_element_located(project.refresh_button_css))
            self.wait.until(EC.presence_of_element_located(project.search_by_name_css))
            self.wait.until(EC.presence_of_element_located(project.create_project_button_css))
            self.wait.until(EC.presence_of_element_located(project.drop_down_css)).click()
            self.wait.until(EC.presence_of_element_located(project.import_from_temp_css))
        except NoSuchElementException:
            pytest.fail("Test Failed")



#python -m pytest test_cases/test_project/test_project_ui.py