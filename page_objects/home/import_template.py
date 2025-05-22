import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_cases.conftest import setup
from test_cases.test_user_login.test_user_login import TestValidLogin
from test_locators.locators import HomePageLocators, ProjectDrawerUILocators, ImportFromTemp
from page_objects.user_login.user_login import ValidUserLogin
from page_objects.home.create_project_drawer import CreateProjectDrawer

home = HomePageLocators
project = ProjectDrawerUILocators
temp = ImportFromTemp


class ImportTemp:
    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login_credentials(self):
        login = TestValidLogin()
        login.test_login_to_account(self.driver)
        time.sleep(5)

    def open_select_from_template_drawer(self):
        self.login_credentials()
        self.wait.until(EC.visibility_of_element_located(home.create_project_xpath))
        self.wait.until(EC.element_to_be_clickable(project.down_element_button_css)).click()
        self.wait.until(EC.presence_of_element_located(project.create_from_temp_button_css)).click()
        time.sleep(1)
        try:
            self.wait.until(EC.presence_of_element_located(project.drawer_title_css))
        except NoSuchElementException:
            pytest.fail("Failed to open 'Select from Template' drawer.")

    def create_project_by_importing_template(self):
        self.open_select_from_template_drawer()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(temp.temp_list_css)).click()
        self.wait.until(EC.presence_of_element_located(temp.create_button_css))
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located(temp.task_list_css))













#python -m pytest test_cases/test_home/test_import_template.py