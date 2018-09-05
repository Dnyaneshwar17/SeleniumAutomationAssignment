import unittest
from testcase.test_login import TestLoginDemo
from testcase.test_create_survey import TestCreateSurvey
from testcase.test_start_survey import TestStartSurvey
from testcase.test_askquestion import TestAskquestionSurvey

class Test_Suite(unittest.TestCase):

    def test_main_class(self):

        self.suite = unittest.TestSuite()
        tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginDemo)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCreateSurvey)
        tc3 = unittest.TestLoader().loadTestsFromTestCase(TestStartSurvey)
        tc4=unittest.TestLoader().loadTestsFromTestCase(TestAskquestionSurvey)

        self.suite.addTests([tc1, tc2, tc3, tc4])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)