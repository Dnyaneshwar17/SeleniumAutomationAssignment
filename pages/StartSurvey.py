from selenium.webdriver.common.by import By
from base.basepage import BasePage
import time

class StartSurvey(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Survey Title Locator
    _survey_title_link="//span[@class='title-text']"
    _new_survey_title = "surveyTitle"
    _survey_save_button = "//*[@id='surveyTitleForm']//a[text()='SAVE']"
    _valid_survey="//div[@id='livePreview']//div[@class='survey-title-table-wrapper']" #change

    #Page Title Locator
    _page_title = "//span[text() = 'PAGE TITLE']"
    _page_title_send ="pageTitle"
    _page_save_button="//form[@id='pageTitleForm']//a[text()='SAVE']"
    _valid_page = "//div[@id='livePreview']//span[@class='page-title user-generated']"

    def survey_title_link(self):
        self.wait_for_element(locator=self._survey_title_link, locator_type="xpath", pollFrequency=1)
        self.element_click(self._survey_title_link, locator_type="xpath")

    def survey_title_send(self,new_survey_title):
        #self.wait_for_element(locator=self._new_survey_title, locator_type="xpath", pollFrequency=1)
        self.clear_field(locator=self._new_survey_title)
        self.send_keys(new_survey_title, self._new_survey_title)

    def save_survey(self):
        self.element_click(self._survey_save_button, locator_type="xpath")

    def survey_title_operation(self, new_survey_title):
        StartSurvey.survey_title_link(self)
        StartSurvey.survey_title_send(self, new_survey_title)
        StartSurvey.save_survey(self)

    def page_title_link(self):
        #self.wait_for_element(locator=self._page_title, locator_type="xpath", pollFrequency=1)
        self.element_click(self._page_title, locator_type="xpath")

    def page_title_send(self, new_page_title):
        #self.wait_for_element(locator=self._page_title_send, locator_type="xpath", pollFrequency=1)
        self.send_keys(new_page_title, self._page_title_send)

    def save_page_title(self):
        self.wait_for_element(locator=self._page_save_button, locator_type="xpath", pollFrequency=1)
        self.element_click(self._page_save_button, locator_type="xpath")

    def page_title_operation(self, new_page_title):
        StartSurvey.page_title_link(self)
        StartSurvey.page_title_send(self, new_page_title)
        StartSurvey.save_page_title(self)

    def start_survey_operation(self, new_survey_title="", new_page_title=""):
        StartSurvey.survey_title_operation(self, new_survey_title)
        time.sleep(5)
        StartSurvey.page_title_operation(self, new_page_title)
        time.sleep(5)
        #StartSurvey.page_title_operation(self, new_page_title)

    # def surveyoperation_successful(self):
    #     self.wait_for_element(locator=self._survey_body, timeout=5, pollFrequency=1)
    #     result = self.is_element_present(locator=self._survey_body)
    #     return result

    def valid_page_title(self):
        time.sleep(5)
        self.wait_for_element(self._valid_page, locator_type="xpath")
        result = self.get_element(locator=self._valid_page, locator_type="xpath").text
        return result

    # def valid_survey_title(self):
    #     time.sleep(5)
    #     self.wait_for_element(self._valid_survey, locator_type="xpath")
    #     result = self.get_element(locator=self._valid_survey, locator_type="xpath").text
    #     return result

        # StartSurvey.survey_title_link(self)
        # StartSurvey.survey_title_send(self,new_survey_title)
        # StartSurvey.save_survey(self)
        # StartSurvey.page_title_link(self)
        # StartSurvey.page_title_send(self,new_page_title)
        # StartSurvey.save_page_title(self)

        #AskQuestion.startquestion(self)


