import pytest
from base.webdriver_factory import Browser_Factory
from pages.Login import Login
from pages.CreateSurvey import CreateSurvey
from utilities_config.Input import*

@pytest.yield_fixture(scope="class")
def one_time_browser_setup():
    get_driver = Browser_Factory(one_time_browser_setup)
    driver = get_driver.select_browser()
    return driver

@pytest.yield_fixture(scope="class")
def start_login():
    get_driver = Browser_Factory(one_time_browser_setup)
    driver = get_driver.select_browser()
    lg = Login(driver)
    lg.startlogin(username, password)
    return driver

@pytest.yield_fixture(scope="class")
def start_survey():
    get_driver = Browser_Factory(one_time_browser_setup)
    driver = get_driver.select_browser()
    lg = Login(driver)
    lg.startlogin(username, password)
    cs = CreateSurvey(driver)
    cs.start_create_survey(first_survey_name)
    return driver