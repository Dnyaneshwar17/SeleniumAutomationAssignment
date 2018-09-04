from pages.AskQuestion import AskQuestion
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import*
import logging

@pytest.mark.usefixtures("start_survey")
class TestAskquestionSurvey(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, start_survey):
        self.question = AskQuestion(start_survey)

    @pytest.mark.run(order=4)
    def test_askquestion(self):
        print("start question on survey")
        self.question.first_question(first_question_enter)

    @pytest.mark.run(order=5)
    def test_question_sec(self):
        print("question_second ")
        self.question.second_question(second_question_enter)

    @pytest.mark.run(order=6)
    def test_question_third(self):
        print("question_third ")
        self.question.third_question(third_question_enter)

    @pytest.mark.run(order=7)
    def test_question_four(self):
        print("question_four ")
        self.question.four_question(four_question_enter)

    @pytest.mark.run(order=8)
    def test_question_five(self):
        print("question_five ")
        self.question.five_question(five_question_enter)

    @pytest.mark.run(order=9)
    def test_question_six(self):
        print("question_six ")
        self.question.six_question(six_question_enter)

    @pytest.mark.run(order=10)
    def test_question_seven(self):
        print("question_seven ")
        self.question.seven_question(seven_question_enter)

    @pytest.mark.run(order=11)
    def test_question_eight(self):
        print("question_eight ")
        self.question.eight_question(eight_question_enter)

    @pytest.mark.run(order=12)
    def test_question_nine(self):
        print("question_nine ")
        self.question.nine_question(nine_question_enter)

    @pytest.mark.run(order=13)
    def test_question_ten(self):
        print("question_second ")
        self.question.ten_question(ten_question_enter)

        # result = self.question.valid_all_question()
        # assert result == True




    # @pytest.mark.run(order=14)
    # def valid_all_question(self):
    #     try:
    #        result = self.question.valid_first_question()
    #        assert (result == True)
    #
    #     except Exception as e:
    #        print("Question Adding Failed" + str(e))
    #
    #    # self.question.valid_second_question()
        # assert (result == True)

        # self.question.valid_third_question()
        # assert (result == True)
        #
        # self.question.valid_four_question()
        # assert (result == True)
        #
        # self.question.valid_five_question()
        # assert (result == True)
        #
        # self.question.valid_six_question()
        # assert (result == True)
        #
        # self.question.valid_seven_question()
        # assert (result == True)
        #
        # self.question.valid_eight_question()
        # assert (result == True)
        #
        # self.question.valid_nini_question()
        # assert (result == True)
        #
        # self.question.valid_ten_question()
        # result = self.ss.valid_page_title()
        # assert result == True


