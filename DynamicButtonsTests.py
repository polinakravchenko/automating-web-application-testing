from DynamicButtonsPages import SearchHelper
from conftest import browser

def test_dynamic_button_page(browser):
    page_button = SearchHelper(browser)
    page_button.go_to_site()
    page_button.click_to_start_button()
    page_button.click_to_one_button()
    page_button.click_to_two_button()
    page_button.click_to_three_button()
    assert page_button.check_result()

