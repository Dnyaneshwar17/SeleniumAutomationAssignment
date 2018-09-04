from pages.CreateSurvey import CreateSurvey
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import *
import logging

@pytest.mark.usefixtures("start_survey")
class TestCreateSurvey(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, start_survey):
        self.sc = CreateSurvey(start_survey)

    @pytest.mark.run(order=2)
    def test_create_survey(self):
        print("start create survey")
        self.sc.start_create_survey(first_survey_name)
        result = self.sc.valid_create_survey()
        assert result == True

