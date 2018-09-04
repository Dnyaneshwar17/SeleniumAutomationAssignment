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
        result = self.question.valid_first_question()
        assert result == str(first_question_enter)

    @pytest.mark.run(order=5)
    def test_question_sec(self):
        print("question second ")
        self.question.second_question(second_question_enter)
        result = self.question.valid_second_question()
        assert result == str(second_question_enter)

    @pytest.mark.run(order=6)
    def test_question_third(self):
        print("question third ")
        self.question.third_question(third_question_enter)
        result = self.question.valid_third_question()
        assert result == str(third_question_enter)

    @pytest.mark.run(order=7)
    def test_question_four(self):
        print("question four ")
        self.question.four_question(four_question_enter)
        result = self.question.valid_four_question()
        assert result == str(four_question_enter)

    @pytest.mark.run(order=8)
    def test_question_five(self):
        print("question five ")
        self.question.five_question(five_question_enter)
        result = self.question.valid_five_question()
        assert result == str(five_question_enter)

    @pytest.mark.run(order=9)
    def test_question_six(self):
        print("question six ")
        self.question.six_question(six_question_enter)
        result = self.question.valid_six_question()
        assert result == str(six_question_enter)

    @pytest.mark.run(order=10)
    def test_question_seven(self):
        print("question seven ")
        self.question.seven_question(seven_question_enter)
        result = self.question.valid_seven_question()
        assert result == str(seven_question_enter)

    @pytest.mark.run(order=11)
    def test_question_eight(self):
        print("question eight ")
        self.question.eight_question(eight_question_enter)
        result = self.question.valid_eight_question()
        assert result == str(eight_question_enter)

    @pytest.mark.run(order=12)
    def test_question_nine(self):
        print("question nine ")
        self.question.nine_question(nine_question_enter)
        result = self.question.valid_nine_question()
        assert result == str(nine_question_enter)

    @pytest.mark.run(order=13)
    def test_question_ten(self):
        print("question second ")
        self.question.ten_question(ten_question_enter)
        result = self.question.valid_ten_question()
        assert result == str(ten_question_enter)
    #drag and drop--------------------------------------------------------------
    @pytest.mark.run(order=14)
    def test_question_drag(self):
        print("drag and drop ")
        self.question.drag_drop_first(four_question_enter)
        result = self.question.valid_four_question()
        assert result == str(four_question_enter)
