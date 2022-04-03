import random

from selenium.webdriver.common.by import By

from universal_ui.universal_ui_actions import UniAct


# def random_selector_for_city():
#     rand_num = random.randint(2, 52)
#     locator = 'contact_form > fieldset > div.form-group.has-feedback.has-success > div > div > select > option:nth-child(' + str(
#         rand_num) + ')'
#     return locator


class ComplexFormPage(UniAct):
    def __init__(self, driver):
        super().__init__(driver)

    # ===============================================================================================
    """ GENERAL ACTION"""

    def get_complex_form_page_title(self, title):
        return self._check_page_title(title)

    # =========================================================================================
    """ FORM SELECTOR"""
    COMPLEX_FORM_SELECTOR = (By.CSS_SELECTOR, '#contact_form > fieldset > legend')
    COMPLEX_FORM_FIRST_NAME = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(2) > div > div > input')
    COMPLEX_FORM_UNDER_FIRST_NAME = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(2) > div > small:nth-child(4)')
    COMPLEX_FORM_LAST_NAME = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(3) > div > div > input')
    COMPLEX_FORM_UNDER_LAST_NAME = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(3) > div > small:nth-child(4)')
    COMPLEX_FORM_EMAIL = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(4) > div > div > input')
    COMPLEX_FORM_UNDER_EMAIL = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(4) > div > small:nth-child(3)')
    COMPLEX_FORM_PHONE = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(5) > div > div > input')
    COMPLEX_FORM_UNDER_PHONE = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(5) > div > small:nth-child(3)')
    COMPLEX_FORM_ADDRESS = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(6) > div > div > input')
    COMPLEX_FORM_UNDER_ADDRESS = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(6) > div > small:nth-child(4)')
    COMPLEX_FORM_CITY = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(7) > div > div > input')
    COMPLEX_FORM_UNDER_CITY = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(7) > div > small:nth-child(4)')
    COMPLEX_FORM_STATE_LIST = (
        By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(8) > div > div > select')
    COMPLEX_FORM_UNDER_STATE_LIST = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(8) > div > small')
    COMPLEX_FORM_ZIP = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(9) > div > div > input')
    COMPLEX_FORM_UNDER_ZIP = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(9) > div > small:nth-child(3)')
    COMPLEX_FORM_WEBSITE = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(10) > div > div > input')
    COMPLEX_FORM_QUESTION_YES = (By.CSS_SELECTOR,
                                 '#contact_form > fieldset > div:nth-child(11) > div > div:nth-child(1) > label > input[type=radio]')
    COMPLEX_FORM_QUESTION_NO = (By.CSS_SELECTOR,
                                '#contact_form > fieldset > div:nth-child(11) > div > div:nth-child(2) > label > input[type=radio]')
    COMPLEX_FORM_DESCRIPTION = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(12) > div > div > textarea')
    COMPLEX_FORM_UNDER_DESCRIPTION = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(12) > div > small:nth-child(4)')
    COMPLEX_FORM_SEND = (By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(14) > div > button')
    COMPLEX_FORM_VALIDATOR = (
        COMPLEX_FORM_SELECTOR, COMPLEX_FORM_FIRST_NAME, COMPLEX_FORM_LAST_NAME, COMPLEX_FORM_EMAIL, COMPLEX_FORM_PHONE,
        COMPLEX_FORM_ADDRESS, COMPLEX_FORM_CITY, COMPLEX_FORM_STATE_LIST, COMPLEX_FORM_ZIP, COMPLEX_FORM_WEBSITE,
        COMPLEX_FORM_QUESTION_YES, COMPLEX_FORM_SEND)
    COMPLEX_FORM_UNDER_VALIDATOR = (COMPLEX_FORM_UNDER_FIRST_NAME, COMPLEX_FORM_UNDER_LAST_NAME, COMPLEX_FORM_UNDER_EMAIL, COMPLEX_FORM_UNDER_PHONE, COMPLEX_FORM_UNDER_ADDRESS, COMPLEX_FORM_UNDER_CITY, COMPLEX_FORM_UNDER_STATE_LIST, COMPLEX_FORM_UNDER_ZIP, COMPLEX_FORM_UNDER_DESCRIPTION)

    def select_complex_form_validation(self):
        return self._validate_multi_visible(self.COMPLEX_FORM_VALIDATOR)

    def select_complex_form_fill_fail(self):
        """ Check unfilled form and return True if there errors on all necessary fields"""
        self._click_single_item(self.COMPLEX_FORM_SEND)
        if not self._validate_multi_visible(self.COMPLEX_FORM_UNDER_VALIDATOR):
            return False
        for element in self.COMPLEX_FORM_UNDER_VALIDATOR:
            print(self._get_element_text(element))
        return True

    def select_complex_form_fill_success(self, account_details):
        """ Fills the form and return true if no errors is visible"""
        state_choice = '#contact_form > fieldset > div:nth-child(8) > div > div > select > option:nth-child('+str(account_details[5])+')'
        state_locator = (By.CSS_SELECTOR, state_choice)
        self._input_text(self.COMPLEX_FORM_FIRST_NAME, account_details[0])
        self._input_text(self.COMPLEX_FORM_LAST_NAME, account_details[0])
        self._input_text(self.COMPLEX_FORM_EMAIL, account_details[1])
        self._input_text(self.COMPLEX_FORM_PHONE, account_details[2])
        self._input_text(self.COMPLEX_FORM_ADDRESS, account_details[0])
        self._input_text(self.COMPLEX_FORM_CITY, account_details[0])
        self._click_single_item(self.COMPLEX_FORM_STATE_LIST)
        self._click_single_item(state_locator)
        self._input_text(self.COMPLEX_FORM_ZIP, account_details[3])
        if account_details[4] == 1:
            self._click_single_item(self.COMPLEX_FORM_QUESTION_YES)
        else:
            self._click_single_item(self.COMPLEX_FORM_QUESTION_NO)
        self._input_text(self.COMPLEX_FORM_DESCRIPTION, account_details[0]+account_details[0])
        self._click_single_item(self.COMPLEX_FORM_SEND)
        if not self._get_multi_invisible_element(self.COMPLEX_FORM_UNDER_VALIDATOR):
            return False
        return True










