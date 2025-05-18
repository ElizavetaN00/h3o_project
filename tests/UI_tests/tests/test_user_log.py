from tests.UI_tests.data_test.creds import SimonUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators, ContactListPageLocators
from tests.UI_tests.pages.base_page import BasePage


def test_valid_credentials(driver):
    headers_contact_list = ["Name", "Birthdate", "Email", "Phone", "Address",
                            "City, State/Province, Postal Code", "Country"]

    valcreds = BasePage(driver, Env.url)
    valcreds.log_in(SimonUserCreds.email,
                    SimonUserCreds.password)
    valcreds.click_button(StartPageLocators.submit_button)

    headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
    headers = [header.text for header in headers_elements]

    assert valcreds.is_url_correct(Env.contact_list_url)
    assert headers == headers_contact_list


def test_empty_form(driver):
    error_msg = "Incorrect username or password"

    e_form = BasePage(driver, Env.url)
    e_form.click_button(StartPageLocators.submit_button)

    assert e_form.get_error_message(StartPageLocators.error_message) == error_msg
