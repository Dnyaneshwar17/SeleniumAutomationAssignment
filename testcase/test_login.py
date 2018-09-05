from pages.Login import Login
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import *
import logging

@pytest.mark.usefixtures("one_time_browser_setup")
class TestLoginDemo(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_browser_setup):
        self.login_start = Login(one_time_browser_setup)

    # @pytest.mark.run(order=1)
    # def test_Failed_Valid(self):
    #     print("InvalidLogin")
    #     self.login_start.startlogin(usernamefaili, password)
    #     result = self.login_start.login_failed()
    #     assert result == True

    @pytest.mark.run(order=1)
    def test_Login_Valid(self):
        print("valid login started")
        self.login_start.startlogin(username, password)
        result = self.login_start.login_successful()
        assert result == True

