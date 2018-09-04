from selenium.webdriver.common.by import By
from base.basepage import BasePage


class CreateSurvey(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _create_first_survey ="CREATE SURVEY"
    _first_survey_title = "surveyTitle"
    _start_survey_scratch="scratch"
    _survey_category_selection = "//div[@class='Select-placeholder']"
    _survey_category_option_selection = "//div[@id='react-select-2--option-0']"
    _save_survey_button = "//button[@class='wds-button' and text()='CREATE SURVEY']"
    _valid_survey = "accQuestionBank" #changes

    def create_survey_link(self):
        self.element_click(self._create_first_survey, locator_type="link")
        return True

    def start_survey_scratch(self):
        self.element_click(self._start_survey_scratch, locator_type="id")

    def send_survey_name(self,first_survey_name):
        self.send_keys(first_survey_name,self._first_survey_title)

    def send_survey_category(self):
        self.element_click(self._survey_category_selection,locator_type="xpath")

    def select_survey_category(self):
        self.element_click(self._survey_category_option_selection ,locator_type="xpath")

    def save_survey(self):
        self.element_click(self._save_survey_button,locator_type="xpath")

    def start_create_survey(self,first_survey_name=""):
        CreateSurvey.create_survey_link(self)
        CreateSurvey.start_survey_scratch(self)
        CreateSurvey.send_survey_name(self,first_survey_name)
        CreateSurvey.send_survey_category(self)
        CreateSurvey.select_survey_category(self)
        CreateSurvey.save_survey(self)

    def valid_create_survey(self):
        self.wait_for_element(locator=self._valid_survey, timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._valid_survey)
        return result

    # def create_survey_successful(self):
    #     self.wait_for_element(locator=self._survey_body, timeout=5, pollFrequency=1)
    #     result = self.is_element_present(locator=self._survey_body)
    #     return result