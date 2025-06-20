import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_cases.conftest import setup
from test_cases.test_user_login.test_user_login import TestValidLogin
from test_locators.locators import ProjectUI

project=ProjectUI

class ProjectInside:
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

    def verify_project_inside_ui (self):
        self.login_credentials()
        self.wait.until(lambda d: d.find_element(*project.construction_project_css)).click()
        self.wait.until(lambda d: d.find_element(*project.subscribe_button_css))
        time.sleep(2)
        self.wait.until(lambda d: d.find_element(*project.project_name_xpath))
        self.wait.until(lambda d: d.find_element(*project.project_refresh_button))
        self.wait.until(lambda d: d.find_element(*project.save_temp_css))
        #self.wait.until(lambda d: d.find_element(*project.settings_button_css))
        #self.wait.until(lambda d: d.find_element(*project.invite_button_css))
        # self.wait.until(lambda d: d.find_element(*project.save_temp_css))
        # self.wait.until(lambda d: d.find_element(*project.project_name_xpath))
        # self.wait.until(lambda d: d.find_element(*project.project_refresh_button))
        # self.wait.until(lambda d: d.find_element(*project.save_temp_css))




#python -m pytest test_cases/test_project_inside/test_project_ui.py