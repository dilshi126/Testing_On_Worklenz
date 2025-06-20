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
        self.wait.until(EC.presence_of_element_located(project.project_tab_css)).click()
        time.sleep(1)

    def search_by_name(self):
        self.login_credentials()
        self.wait.until(EC.presence_of_element_located(project.search_by_name_css)).send_keys("Edu")
        self.wait.until(EC.presence_of_element_located(project.edu_row_css))

    def search_from_favourite(self):
        self.login_credentials()
        self.wait.until(EC.presence_of_element_located(project.project_tab_css)).click()
        self.wait.until(EC.presence_of_element_located(project.favourite_tab_css)).click()
        self.wait.until(EC.presence_of_element_located(project.search_by_name_css)).send_keys("Edu")
        self.wait.until(EC.presence_of_element_located(project.edu_row_css))

    def search_from_archive(self):
        self.login_credentials()

        self.wait.until(lambda d: d.find_element(*project.project_tab_css)).click()
        self.wait.until(lambda d: d.find_element(*project.archive_tab_css)).click()
        self.wait.until(lambda d: d.find_element(*project.search_by_name_css)).send_keys("personal")
        self.wait.until(lambda d: d.find_element(*project.personal_xpath))


#python -m pytest test_cases/test_project/test_project_search_functionality.py