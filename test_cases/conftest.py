import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utilities import ReadConfigurations


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver



# def setup(request):
#     browser = ReadConfigurations.read_configuration("basic info", "browser")
#
#
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome()
#     elif browser.lower() == "firefox":
#         driver = webdriver.Firefox()
#     elif browser.lower() == "edge":
#         driver = webdriver.Edge()
#     else:
#         raise Exception("Provide a valid browser name: chrome / firefox / edge")
#
#     driver.maximize_window()
#
#     app_url = ReadConfigurations.read_configuration("basic info", "url")
#     driver.get(app_url)
#
#     request.cls.driver = driver
#     yield
#     driver.quit()
