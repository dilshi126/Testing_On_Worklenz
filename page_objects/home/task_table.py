import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_cases.conftest import setup
from test_cases.test_user_login.test_user_login import TestValidLogin
from test_locators.locators import HomePageLocators, ProjectDrawerUILocators, ImportFromTemp,TaskTable

taskTable=TaskTable

class TaskTable:
    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login_credentials(self):
        login = TestValidLogin()
        login.test_login_to_account(self.driver)
        time.sleep(5)

    def visibility_of_add_a_task(self):
        self.login_credentials()
        self.wait.until(EC.presence_of_element_located(taskTable.add_task_button_css))

#python -m pytest test_cases/test_home/test_task_table.py