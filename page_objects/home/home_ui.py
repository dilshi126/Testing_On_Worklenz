import time
from selenium import webdriver
import pytest
from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_cases.conftest import setup
from test_cases.test_user_login.test_user_login import TestValidLogin
from test_locators.locators import HomePageLocators, ProjectDrawerUILocators
from page_objects.user_login.user_login import ValidUserLogin



home = HomePageLocators



class HomePageUI:
    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login_credentials(self):
        login= TestValidLogin()
        login.test_login_to_account(self.driver)
        time.sleep(5)


    def verify_home_ui(self):
        self.login_credentials()

        try:
           self.wait.until(EC.visibility_of_element_located(home.nav_bar_xpath))
           self.wait.until(EC.presence_of_element_located(home.invite_button_xpath))
           self.wait.until(EC.presence_of_element_located(home.help_button_xpath))
           self.wait.until(EC.presence_of_element_located(home.profile_xpath))
           self.wait.until(EC.presence_of_element_located(home.create_project_xpath))
           self.wait.until(EC.element_to_be_clickable(home.expan_button_css)).click()
           self.wait.until(EC.presence_of_element_located(home.import_template_xpath))
           self.wait.until(EC.presence_of_element_located(home.name_xpath))
           self.wait.until(EC.presence_of_element_located(home.date_css))
           self.wait.until(EC.presence_of_element_located(home.task_table_xpath))
           self.wait.until(EC.presence_of_element_located(home.list_tab_xpath))
           self.wait.until(EC.element_to_be_clickable(home.calender_tab_xpath)).click()
           self.wait.until(EC.element_to_be_clickable(home.Month_xpath)).click()
           try:
               self.wait.until(EC.presence_of_element_located(home.current_year_xpath))
               self.wait.until(EC.presence_of_element_located(home.current_month_xpath))
           except NoSuchElementException:
                pytest.fail("Test case is failed")
           self.wait.until(EC.presence_of_element_located(home.year_xpath))
           self.wait.until(EC.presence_of_element_located(home.assigned_to_me_button_xpath))
           self.wait.until(EC.presence_of_element_located(home.refresh_button_xpath))
           self.wait.until(EC.presence_of_element_located(home.to_do_list_xpath))
           self.wait.until(EC.presence_of_element_located(home.add_task_todo_xpath))
           self.wait.until(EC.presence_of_element_located(home.todo_refresh_xpath))
           self.wait.until(EC.presence_of_element_located(home.project_table_xpath))
           self.wait.until(EC.presence_of_element_located(home.favourite_icon_xpath))
           self.wait.until(EC.presence_of_element_located(home.recent_tab_xpath))
           self.wait.until(EC.presence_of_element_located(home.favourite_tab_xpath))
           self.wait.until(EC.presence_of_element_located(home.favourite_icon_xpath))
           self.wait.until(EC.presence_of_element_located(home.project_refresh_xpath))
           print ("Test passed")
        except TimeoutException:
            print("Test failed")
            time.sleep(1)


    time.sleep(1)
    def tooltips_on_home_page(self):
        self.login_credentials()

        tooltip_data = [
            ("//button[.//span[@aria-label='bell']]", "View notifications")
            ]


        for xpath, expected_text in tooltip_data:
            target_element = self.driver.find_element(By.XPATH, xpath)
            ActionChains(self.driver).move_to_element(target_element).perform()
            time.sleep(1)

            tooltip = self.driver.find_element(By.CLASS_NAME, "ant-tooltip-inner")
            tooltip_text = tooltip.text
            print("Tooltip text:", tooltip_text)
            time.sleep(1)






#python -m pytest test_cases/test_home/test_home_ui.py