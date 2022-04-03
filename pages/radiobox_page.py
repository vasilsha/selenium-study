from selenium.webdriver.common.by import By
from universal_ui.universal_ui_actions import UniAct


class RadioPage(UniAct):
    def __init__(self, driver):
        super().__init__(driver)

    # ===============================================================================================
    """ GENERAL ACTION"""

    def get_checkbox_page_title(self, title):
        return self._check_page_title(title)

    # ==============================================================================================
    """SINGLE RADIO"""
    SINGLE_RADIO_HEADER = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(4) > div.panel-heading')
    SINGLE_RADIO_MALE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(4) > div.panel-body > label:nth-child(2) > input[type=radio]')
    SINGLE_RADIO_FEMALE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(4) > div.panel-body > label:nth-child(3) > input[type=radio]')
    SINGLE_RADIO_GET_CHECKED = (By.CSS_SELECTOR, '#buttoncheck')
    SINGLE_RADIO_GET_MESSAGE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(4) > div.panel-body > p.radiobutton')
    SINGLE_RADIO_VALIDATOR = (SINGLE_RADIO_HEADER, SINGLE_RADIO_MALE, SINGLE_RADIO_FEMALE, SINGLE_RADIO_GET_CHECKED)

    def select_single_radio_validation(self):
        return self._validate_multi_visible(self.SINGLE_RADIO_VALIDATOR)

    def select_single_radio(self):
        self._click_single_item(self.SINGLE_RADIO_GET_CHECKED)
        message = self._get_element_text(self.SINGLE_RADIO_GET_MESSAGE)
        print(message)
        if message != "Radio button is Not checked":
            return False
        self._click_single_item(self.SINGLE_RADIO_MALE)
        self._click_single_item(self.SINGLE_RADIO_GET_CHECKED)
        message = self._get_element_text(self.SINGLE_RADIO_GET_MESSAGE)
        print(message)
        if message != "Radio button 'Male' is checked":
            return False
        self._click_single_item(self.SINGLE_RADIO_FEMALE)
        self._click_single_item(self.SINGLE_RADIO_GET_CHECKED)
        message = self._get_element_text(self.SINGLE_RADIO_GET_MESSAGE)
        print(message)
        if message == "Radio button 'Female' is checked":
            return True
        return False


    # ==============================================================================================
    """MULTIPLE RADIO"""
    MULTIPLE_RADIO_HEADER = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-heading')
    MULTIPLE_RADIO_MALE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(2) > label:nth-child(2) > input[type=radio]')
    MULTIPLE_RADIO_FEMALE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(2) > label:nth-child(3) > input[type=radio]')
    MULTIPLE_RADIO_AGE_0_5 = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(3) > label:nth-child(2) > input[type=radio]')
    MULTIPLE_RADIO_AGE_5_15 = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(3) > label:nth-child(3) > input[type=radio]')
    MULTIPLE_RADIO_AGE_15_50 = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(3) > label:nth-child(4) > input[type=radio]')
    MULTIPLE_RADIO_GET_VALUE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > button')
    MULTIPLE_RADIO_MESSAGE = (By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > p.groupradiobutton')
    MULTIPLE_RADIO_VALIDATOR = (MULTIPLE_RADIO_HEADER, MULTIPLE_RADIO_MALE, MULTIPLE_RADIO_FEMALE, MULTIPLE_RADIO_AGE_0_5, MULTIPLE_RADIO_AGE_5_15, MULTIPLE_RADIO_AGE_15_50, MULTIPLE_RADIO_GET_VALUE)

    def select_multiple_radio_validation(self):
        return self._validate_multi_visible(self.MULTIPLE_RADIO_VALIDATOR)

    def select_multiple_radio(self):
        self._click_single_item(self.MULTIPLE_RADIO_MALE)
        self._click_single_item(self.MULTIPLE_RADIO_AGE_0_5)
        self._click_single_item(self.MULTIPLE_RADIO_GET_VALUE)
        message = self._get_element_text(self.MULTIPLE_RADIO_MESSAGE).split('\n')
        msg1 = message[0]
        msg2 = message[1]
        print(msg1, '|must be :"Sex : Male"')
        print(msg2, '|must be :"Age group: 0 - 5"')
        self._click_single_item(self.MULTIPLE_RADIO_FEMALE)
        self._click_single_item(self.MULTIPLE_RADIO_AGE_5_15)
        self._click_single_item(self.MULTIPLE_RADIO_GET_VALUE)
        message = self._get_element_text(self.MULTIPLE_RADIO_MESSAGE).split('\n')
        msg3 = message[0]
        msg4 = message[1]
        print(msg3, '|must be :"Sex : Female"')
        print(msg4, '|must be :"Age group: 15 - 50"')
        self._click_single_item(self.MULTIPLE_RADIO_AGE_15_50)
        self._click_single_item(self.MULTIPLE_RADIO_GET_VALUE)
        message = self._get_element_text(self.MULTIPLE_RADIO_MESSAGE).split('\n')
        msg5 = message[1]
        print(msg5, '|must be :"Sex : Male"')
        # check that all messages are what was select
        if msg1 == "Sex : Male" and msg2 == 'Age group: 0 - 5' and msg3 == "Sex : Female" and msg4 == 'Age group: 5 - 15' and msg5 == 'Age group: 15 - 50':
            return True
        return False
