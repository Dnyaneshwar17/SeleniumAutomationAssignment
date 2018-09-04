import pytest
from utilities_config.Input import*
from base.webdriver_factory import Browser_Factory
from pages.Login import Login
from pages.CreateSurvey import CreateSurvey
from pages.StartSurvey import StartSurvey
from pages.AskQuestion import AskQuestion

@pytest.fixture(scope='module')
def select_driver():
    select_driver = Browser_Factory("chrome")
    driver = select_driver.select_browser()
    return driver

@pytest.mark.run(order=1)
def test_validLogin(select_driver):
    print("Valid Login Stared")
    lp = Login(select_driver)
    lp.startlogin(username, password)
    result = lp.login_successful()
    print("Result: " + str(result))

    assert result == True

@pytest.mark.run(order=2)
def test_create_survey(select_driver):
    print("create survey started")
    cs = CreateSurvey(select_driver)
    cs.start_create_survey(first_survey_name)
    result = cs.valid_create_survey()
    print("Result: " + str(result))

    assert result == True

@pytest.mark.run(order=3)
def test_survey_operation(select_driver):
    print("survey operation started")
    operation_survey = StartSurvey(select_driver)
    operation_survey.start_survey_operation(new_survey_title, new_page_title)
    result = operation_survey.valid_page_title()
    print("Result: " + str(result))
    assert result == str(new_page_title)


@pytest.mark.run(order=4)
def test_question_first(select_driver):
    print("first question ")
    questions_first = AskQuestion(select_driver)
    questions_first.first_question(first_question_enter)
    result = questions_first.valid_first_question()
    print("Result: " + str(result))
    assert result == str(first_question_enter)

@pytest.mark.run(order=5)
def test_question_2(select_driver):
    print("second question ")
    questions_second = AskQuestion(select_driver)
    questions_second.second_question(second_question_enter)
    result = questions_second.valid_second_question()
    print("Result: " + str(result))
    assert result == str(second_question_enter)



@pytest.mark.run(order=6)
def test_question_4(select_driver):
    print("four question")
    questions_four = AskQuestion(select_driver)
    questions_four.four_question(four_question_enter)
    result = questions_four.valid_four_question()
    print("Result: " + str(result))
    assert result == str(four_question_enter)



@pytest.mark.run(order=7)
def test_question_10(select_driver):
    print("ten question")
    questions_ten = AskQuestion(select_driver)
    questions_ten.ten_question(ten_question_enter)
    result = questions_ten.valid_ten_question()
    print("Result: " + str(result))
    assert result == str(ten_question_enter)

@pytest.mark.run(order=8)
def test_question_3(select_driver):
    print("third question")
    questions_third = AskQuestion(select_driver)
    questions_third.third_question(third_question_enter)
    result = questions_third.valid_third_question()
    print("Result: " + str(result))
    assert result == str(third_question_enter)


@pytest.mark.run(order=9)
def test_question_5(select_driver):
    print("five question")
    questions_five = AskQuestion(select_driver)
    questions_five.five_question(five_question_enter)
    result = questions_five.valid_five_question()
    print("Result: " + str(result))
    assert result == str(five_question_enter)

@pytest.mark.run(order=10)
def test_question_9(select_driver):
    print(" nine question ")
    questions_nine = AskQuestion(select_driver)
    questions_nine.nine_question(nine_question_enter)
    result = questions_nine.valid_nine_question()
    print("Result: " + str(result))
    assert result == str(nine_question_enter)


@pytest.mark.run(order=11)
def test_question_6(select_driver):
        print(" six question ")
        questions_six = AskQuestion(select_driver)
        questions_six.six_question(six_question_enter)
        result = questions_six.valid_six_question()
        print("Result: " + str(result))
        assert result == str(six_question_enter)

@pytest.mark.run(order=12)
def test_question_8(select_driver):
        print(" eight question ")
        questions_eight = AskQuestion(select_driver)
        questions_eight.eight_question(eight_question_enter)
        result = questions_eight.valid_eight_question()
        print("Result: " + str(result))
        assert result == str(eight_question_enter)

@pytest.mark.run(order=13)
def test_question_7(select_driver):
        print(" seven question ")
        questions_seven = AskQuestion(select_driver)
        questions_seven.seven_question(seven_question_enter)
        result = questions_seven.valid_seven_question()
        print("Result: " + str(result))
        assert result == str(seven_question_enter)


@pytest.mark.run(order=14)
def test_drag_drop(select_driver):
    question_drag_drop = AskQuestion(select_driver)
    question_drag_drop.drag_drop_first(four_question_enter)
    result = question_drag_drop.valid_four_question()
    print("Result: " + str(result))
    assert result == str(four_question_enter)


