from base.basepage import BasePage
from utilities_config.Input import*
import time

class AskQuestion(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _enter_question = "editTitle"
    _enter_question_type = "changeQType"
    _question_save_button = "//div[@id='editQuestion']/section[@class='t1']//a[text()='SAVE']"
    _add_new_question = "//a[.='NEW QUESTION']"
    _survey_body = "create"

    first_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Single Textbox']"

    #valid_que_1 = "question-container"
    #valid_que_1 ="question-title-container"

    #valid_que_1 = "user-generated notranslate"
    #valid_que_1 = "question-essay qn question essay"
    valid_que_1 = "//span[@class='user-generated notranslate']"
    cancle_button = "//a[@class='wds-button wds-button--sm wds-button--ghost cancel']"



    # Second Question:
    second_question_pattern = "//ul[@class='add-q-menu-right']//a[text()='Date / Time']"
    second_question_select_pattern = "//table[@id='rows']/tfoot[@class='answerTableFooter']//label[.='Time Info']"
    valid_que_2 = "//input[@class='form-control text']"

      # Third Question:

    third_nine_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
    third_nine_question_select_pattern = "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
    third_question_select_specific = "//option[contains(text(),'Always - Never')]"
    valid_que_3 = "//span[text()='How often do you use SurveyMonkey?']"

      # Four Question:
    four_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Star Rating']"
    valid_que_4 ="//div[@class='question-emoji-rating  qn question rating']"

      # Five Question:
    five_question_pattern = "//ul[@class='add-q-menu-right']//a[text()='Dropdown']"
    five_nine_question_select_specific = "//option[contains(text(),'Yes - No')]"
    valid_que_5 = "//span[text()='Did you get meaningful data from survey analysis?']"
    valid_que_9 = " //span[text()='Will recommend SurveyMonkey to your friends / Colleagues?']"

   #Drag and Drop six question

    select_builder = "li[@class='nav-tabs-select-style']"
    click_dropdown = "span[@class='listText' and text()='Dropdown']"



    #Six Question:
    valid_que_6="//span[text()='Check the Features you like about SurveyMonkey?']"
    six_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Checkboxes']"
    six_question_1 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[4]/td[2]/div/div[1]"
    six_question_2 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[5]/td[2]/div/div[1]"
    six_question_3 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[6]/td[2]/div/div[1]"
    six_question_4 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[7]/td[2]/div/div[1]"
    six_question_5 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[8]/td[2]/div/div[1]"

    # seven question
    valid_que_7="//span[text()='Rate our features. (Matrix Rating Scale)']"
    seven_question_pattern = "//ul[@class='add-q-menu-right']//a[text()='Matrix / Rating Scale']"
    seven_question_1 = "//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[3]/td[1]/div/div[1]"
    seven_question_2 = "//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[4]/td[1]/div/div[1]"
    seven_question_3 = "//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[5]/td[1]/div/div[1]"
    seven_question_4 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[2]/td[1]/div/div[1]"
    seven_question_5 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[3]/td[1]/div/div[1]"
    seven_question_6 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[4]/td[1]/div/div[1]"
    seven_question_7 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[5]/td[1]/div/div[1]"

    #Eight Question
    valid_que_8="//span[text()='List the features you like most.']"
    eight_question_pattern="//ul[@class='add-q-menu-right']//a[text()='Multiple Textboxes']"
    eight_question_1 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[3]/td[1]/div/div[1]"
    eight_question_2 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[4]/td[1]/div/div[1]"
    eight_question_3 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[5]/td[1]/div/div[1]"
    eight_question_4 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[6]/td[1]/div/div[1]"
    eight_question_5 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[7]/td[1]/div/div[1]"

    # Ten Question
    ten_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Comment Box']"
    valid_que_10 = "//span[text()='Comments / Feedback (Text-area)']"


    #Drag and Drop
    click_drag_drop = "//div[@class='add-question-btn zero-state-hide ui-droppable']"
    question_edit = "editQuestion"
    question_first_type = "//span[@class='listText' and text()='Star Rating']"
    click_select_box = "//li[@title='Builder']"
    #click_select_box = "//li[@class='nav-tabs-select-style']"
    question_type = "editQuestion"
    question_set = "changeQType"



    def save_button(self):
        self.wait_for_element(locator=self._question_save_button, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._question_save_button, locator_type="xpath")

    def next_question(self):
        self.wait_for_element(locator=self._add_new_question, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._add_new_question, locator_type="xpath")

    def enter_question_type(self):
        self.element_click(self._enter_question_type)

    # def commonall_question_pattern(self):
    #     self.element_click(self.third_nine_question_pattern)
    #
    # def commonall_question_select_pattern(self):
    #     self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
    #     self.element_click(self.third_nine_question_select_pattern)

    def drag_drop_first(self, four_question_enter):
        self.element_click(self.click_select_box, locator_type="xpath")
        self.web_scroll(direction="down")
        self.drag_drop(self.question_first_type, self.click_dropdown, locator_type="xpath")
        self.element_click(self.question_set)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(four_question_enter, self._enter_question)
        AskQuestion.save_button(self)

    def first_question(self, first_question_enter=""):
        #time.sleep(5)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(first_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.wait_for_element(locator=self.first_question_pattern, timeout=5, pollFrequency=1)
        self.element_click(self.first_question_pattern, locator_type="xpath")
        AskQuestion.save_button(self)
        #AskQuestion.next_question(self)

    def second_question(self, second_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(second_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.second_question_pattern, locator_type="xpath")
        self.element_click(self.second_question_select_pattern, locator_type="xpath")
        AskQuestion.save_button(self)

    def four_question(self, four_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(four_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.four_question_pattern, locator_type="xpath")
        AskQuestion.save_button(self)

    def third_question(self, third_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(third_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.third_nine_question_pattern, locator_type="xpath")
        self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
        self.element_click(self.third_nine_question_select_pattern, locator_type="xpath")
        self.element_click(self.third_question_select_specific, locator_type="xpath")
        AskQuestion.save_button(self)

    def five_question(self, five_question=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(five_question, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.five_question_pattern, locator_type="xpath")
        self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
        self.element_click(self.third_nine_question_select_pattern, locator_type="xpath")
        self.element_click(self.five_nine_question_select_specific, locator_type="xpath")
        AskQuestion.save_button(self)

    def nine_question(self, nine_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(nine_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.third_nine_question_pattern, locator_type="xpath")
        self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
        self.element_click(self.third_nine_question_select_pattern, locator_type="xpath")
        self.element_click(self.five_nine_question_select_specific, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def ten_question(self, ten_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(ten_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.wait_for_element(locator=self.ten_question_pattern, timeout=5, pollFrequency=1)
        self.element_click(self.ten_question_pattern, locator_type="xpath")
        AskQuestion.save_button(self)

    def six_question(self, six_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(six_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.six_question_pattern, locator_type="xpath")
        AskQuestion.six_question_special_type(self)
        AskQuestion.save_button(self)

    def six_question_special_type(self):
        self.send_keys(six_1, self.six_question_1, locator_type="xpath")
        self.send_keys(six_2, self.six_question_2, locator_type="xpath")
        self.send_keys(six_3, self.six_question_3, locator_type="xpath")
        self.send_keys(six_4, self.six_question_4, locator_type="xpath")
        self.send_keys(six_5, self.six_question_5, locator_type="xpath")

    def seven_question(self, seven_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(seven_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.wait_for_element(locator=self.seven_question_pattern, locator_type="xpath", pollFrequency=1)
        self.element_click(self.seven_question_pattern, locator_type="xpath")
        AskQuestion.seven_question_special_type(self)
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def seven_question_special_type(self):
        self.send_keys(seven_1, self.seven_question_1, locator_type="xpath")
        self.send_keys(seven_2, self.seven_question_2, locator_type="xpath")
        self.send_keys(seven_3, self.seven_question_3, locator_type="xpath")
        self.send_keys(seven_4, self.seven_question_4, locator_type="xpath")
        self.send_keys(seven_5, self.seven_question_5, locator_type="xpath")
        self.send_keys(seven_6, self.seven_question_6, locator_type="xpath")
        self.send_keys(seven_7, self.seven_question_7, locator_type="xpath")

    def eight_question(self, eight_question_enter=""):
        #time.sleep(5)
        AskQuestion.next_question(self)
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        self.send_keys(eight_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.wait_for_element(locator=self.eight_question_pattern, locator_type="xpath", pollFrequency=1)
        self.element_click(self.eight_question_pattern, locator_type="xpath")
        AskQuestion.eight_question_special_type(self)
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def eight_question_special_type(self):
        self.send_keys(six_1, self.eight_question_1, locator_type="xpath")
        self.send_keys(six_2, self.eight_question_2, locator_type="xpath")
        self.send_keys(six_3, self.eight_question_3, locator_type="xpath")
        self.send_keys(six_4, self.eight_question_4, locator_type="xpath")
        self.send_keys(six_5, self.eight_question_5, locator_type="xpath")

    # def drag_drop_first(self, four_question=" "):
    #     time.sleep(5)
    #     self.element_click(self._click_select_box, locator_type="xpath")
    #     time.sleep(3)
    #     self.element_click(self._first_question_type,locator_type="xpath")
    #     time.sleep(3)
    #     self.element_click(self._click_drag_drop,locator_type="xpath")
    #     time.sleep(3)
    #     # self.element_click(self._question_edit,locator_type="id")
    #     # time.sleep(3)
    #     self.send_keys(four_question, self._enter_question)
    #     AskQuestion.save_button(self)


    # def verify_question(self):
    #     self.wait_for_element(locator=self._survey_body, timeout=5, pollFrequency=1)
    #     result = self.is_element_present(locator=self._survey_body)
    #     return result
    def valid_first_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_1, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_1, locator_type="xpath")
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        result = self.get_element(locator=self._enter_question, locator_type="id").text
        self.element_click(self.cancle_button, locator_type="xpath")
        if result == (first_question_enter):
          return result
        else:
            result = False
            return result

    def valid_second_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_2, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_2, locator_type="xpath")
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        result = self.get_element(locator=self._enter_question, locator_type="id").text
        self.wait_for_element(locator=self.cancle_button, timeout=5, pollFrequency=1)
        self.element_click(self.cancle_button, locator_type="xpath")
        if result == (second_question_enter):
            print("result for second:"+result)
            return result
        else:
            result = False
            return result

    def valid_third_question(self):
        self.wait_for_element(locator=self.valid_que_3, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_3, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (third_question_enter):
            print("result for third:" + result)
            return result
        else:
            result = False
            return result

    def valid_four_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_4, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_4, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (four_question_enter):
            print("result for four:" + result)
            return result
        else:
            result = False
            return result

    def valid_five_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_5, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_5, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (five_question_enter):
            print("result for five:" + result)
            return result
        else:
            result = False
            return result

    def valid_six_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_6, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_6, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (six_question_enter):
            print("result for six:" + result)
            return result
        else:
            result = False
            return result

    def valid_eight_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_8, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_8, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (eight_question_enter):
            print("result for six:" + result)
            return result
        else:
            result = False
            return result

    def valid_seven_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_7, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_7, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (seven_question_enter):
            print("result for six:" + result)
            return result
        else:
            result = False
            return result

    def valid_nine_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_9, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_9, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (nine_question_enter):
            print("result for nine:" + result)
            return result
        else:
            result = False
            return result

    def valid_ten_question(self):
        time.sleep(5)
        self.wait_for_element(locator=self.valid_que_10, timeout=5, pollFrequency=1)
        self.element_click(self.valid_que_10, locator_type="xpath")
        result = AskQuestion.valid_common_toAll(self)
        if result == (ten_question_enter):
            print("result for ten:" + result)
            return result
        else:
            result = False
            return result

    def valid_common_toAll(self):
        self.wait_for_element(locator=self._enter_question, timeout=5, pollFrequency=1)
        result = self.get_element(locator=self._enter_question, locator_type="id").text
        self.wait_for_element(locator=self.cancle_button, timeout=5, pollFrequency=1)
        self.element_click(self.cancle_button, locator_type="xpath")
        return result


