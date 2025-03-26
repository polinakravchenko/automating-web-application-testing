from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()