import time
import pytest
from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
import random
from test_cases.conftest import setup
from test_cases.test_user_login.test_user_login import TestValidLogin
from test_locators.locators import HomePageLocators, ProjectDrawerUILocators, CreatedProject
from page_objects.user_login.user_login import ValidUserLogin
from test_data.test_data import ProjectCreation
from selenium.webdriver.common.by import By

home = HomePageLocators
project=ProjectDrawerUILocators
locators=CreatedProject
data=ProjectCreation


class CreateProjectDrawer:
    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.faker = Faker()

    def login_credentials(self):
        login= TestValidLogin()
        login.test_login_to_account(self.driver)
        time.sleep(5)

    def verify_open_create_project_drawer(self):
        self.login_credentials()
        self.wait.until(EC.visibility_of_element_located(home.create_project_xpath)).click()
        try:
            self.wait.until(EC.presence_of_element_located(home.create_project_drawer_xpath))
            print("Test case passed")
        except NoSuchElementException:
            pytest.fail("Test case failed")

    def verify_project_drawer_ui(self):
        self.verify_open_create_project_drawer()
        try:
            self.wait.until(EC.visibility_of_element_located(project.name_field_xpath))
            self.wait.until(EC.presence_of_element_located(project.colour_dropdown_id))
        except NoSuchElementException:
            pytest.fail("Test case failed")


    def creating_new_project(self):
        project_details = {
            "project_name" : "",
            "project_color":"",
            "project_status":"",
            "project_health":"",
            "project_category":"",
            "project_notes":"",
            "project_client":"",
            "project_manager":"",
            "start_date":"",
            "end_date":"",
            "estimate_working_days":"",
            "estimate_man_days":"",
            "hours_per_day":""
        }
        self.verify_open_create_project_drawer()

        # project_name = self.faker.name()
        # self.wait.until(EC.presence_of_element_located(project.name_field_xpath)).send_keys(project_name)
        # project_details["project_name"] = project_name
        # time.sleep(1)

        time.sleep(1)
        project_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
        self.wait.until(EC.presence_of_element_located(project.colour_dropdown_css)).click()
        color_input = self.wait.until(EC.visibility_of_element_located(project.color_picker_css))
        print("Color input found:", color_input)
        color_input.clear()
        color_input.send_keys(project_color)
        self.wait.until(EC.presence_of_element_located(project.colour_dropdown_css)).click()
        time.sleep(0.5)
        project_details["project_color"] = project_color
        time.sleep(1)

        project_name = self.faker.name()
        name_input = self.wait.until(EC.presence_of_element_located(project.name_field_xpath))
        name_input.click()
        name_input.clear()
        name_input.send_keys(project_name)
        name_input.send_keys(Keys.TAB)
        project_details["project_name"] = project_name

        create_button = self.wait.until(EC.element_to_be_clickable(project.create_project_xpath))
        self.driver.execute_script("arguments[0].click();", create_button)
        time.sleep(5)

        self.wait.until(EC.presence_of_element_located(locators.back_button_css)).click()
        time.sleep(5)

        self.wait.until(EC.presence_of_element_located(locators.table_header_name_css))

        table_rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        project_names = [row.text for row in table_rows]
        print("Project names found in table:", project_names)
        assert any(project_name in row for row in project_names), f"Project '{project_name}' not found in table after creation"



        # categories = ['Finance', 'Healthcare', 'E-commerce', 'Education', 'Logistics', 'Marketing', 'SaaS']
        # project_category = random.choice(categories)
        # self.wait.until(EC.presence_of_element_located(project.project_category_css)).click()
        # time.sleep(1)
        # self.wait.until(EC.visibility_of_element_located(project.add_category_button_css)).click()
        # time.sleep(1)
        # self.wait.until(EC.presence_of_element_located(project.project_category_css)).send_keys(project_category)
        # project_details["project_category"] = project_category
        # time.sleep(1)

        # project_notes = self.faker.sentence()
        # note_field = self.wait.until(EC.element_to_be_clickable(project.project_note_xpath))
        # note_field.click()  # Optional, only if needed
        # note_field.send_keys(project_notes)
        # project_details["project_notes"] = project_notes


    def verify_required_fields_when_creating_new_project(self):
        self.verify_open_create_project_drawer()
        self.wait.until(EC.presence_of_element_located(project.create_project_xpath)).click()
        try:
            self.wait.until(EC.presence_of_element_located(project.name_empty_error_css))
        except NoSuchElementException:
            pytest.fail("test failed")













#python -m pytest test_cases/test_home/test_create_project_drawer.py

