from BaseApp import BaseApp
from selenium.webdriver.common.by import By

class DynamicButtonsLocator:

    BUTTON_START_LOCATOR = (By.ID, "button00")
    BUTTON_ONE_LOCATOR = (By.ID, "button01")
    BUTTON_TWO_LOCATOR = (By.ID, "button02")
    BUTTON_THREE_LOCATOR = (By.ID, "button03")

    TEXT_RESULT_LOCATOR = (By.XPATH, "//p[contains(text(), 'All Buttons Clicked')]")

class SearchHelper(BaseApp):

    def click_to_start_button(self):
        self.is_enabled(DynamicButtonsLocator.BUTTON_START_LOCATOR, time=5)
        return self.find_element(DynamicButtonsLocator.BUTTON_START_LOCATOR, time=5).click()

    def click_to_one_button(self):
        self.is_enabled(DynamicButtonsLocator.BUTTON_ONE_LOCATOR, time=5)
        return self.find_element(DynamicButtonsLocator.BUTTON_ONE_LOCATOR, time=5).click()

    def click_to_two_button(self):
        self.is_enabled(DynamicButtonsLocator.BUTTON_TWO_LOCATOR, time=5)
        return self.find_element(DynamicButtonsLocator.BUTTON_TWO_LOCATOR, time=5).click()

    def click_to_three_button(self):
        self.is_enabled(DynamicButtonsLocator.BUTTON_THREE_LOCATOR, time=7)
        return self.find_element(DynamicButtonsLocator.BUTTON_THREE_LOCATOR, time=7).click()

    def check_result(self):
        return self.find_element(DynamicButtonsLocator.TEXT_RESULT_LOCATOR, time=1).is_displayed()