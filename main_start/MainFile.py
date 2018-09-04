from pages.StartSurvey import StartSurvey
from utilities_config.Browser import BrowserConfig
from pages.Login import Login
from pages.CreateSurvey import CreateSurvey
from pages.StartSurvey import StartSurvey
from base.webdriver_factory import Browser_Factory
from pages.AskQuestion import AskQuestion
from utilities_config.Input import*
import time

class Start():

    def __init__(self):
        get_driver = Browser_Factory()
        self.driver = get_driver.select_browser()

    def start_app(self):

        log = Login(self.driver)
        log.startlogin(username, password)
        cre_survey = CreateSurvey(self.driver)
        cre_survey.start_create_survey(first_survey_name)

        sur_operation = StartSurvey(self.driver)
        sur_operation.start_survey_operation(new_survey_title, new_page_title)

        enter_questions = AskQuestion(self.driver)
        enter_questions.first_question(first_question_enter)
        enter_questions.second_question(second_question_enter)
        enter_questions.third_question(third_question_enter)
        enter_questions.four_question(four_question_enter)

        # enter_questions = AskQuestion(self.driver)
        # enter_questions.question(first_question)
        # # enter_questions.second_question(second_question)
        # enter_questions.third_question(third_question)
        # enter_questions.four_question(four_question)
        # enter_questions.first_question(five_question)
        #




start = Start()
start.start_app()

