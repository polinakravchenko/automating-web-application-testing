from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class BaseApp:
    def __init__(self, driver):
        self.url = "https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html"
        self.driver = driver

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    def is_enabled(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))