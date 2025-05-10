from tests.UI_tests.data_test.creds import AddUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators, AddUserLocators, ContactListPageLocators
from tests.UI_tests.pages.base_page import BasePage


def test_valid_credentials(driver):
    headers_contact_list = ["Name", "Birthdate", "Email", "Phone", "Address",
                            "City, State/Province, Postal Code", "Country"]

    valcreds = BasePage(driver, Env.url)
    valcreds.open()
    valcreds.click_button(StartPageLocators.sign_up_button)
    valcreds.send_text(AddUserLocators.first_name, AddUserCreds.first_name)
    valcreds.send_text(AddUserLocators.last_name, AddUserCreds.last_name)
    valcreds.send_text(AddUserLocators.email, AddUserCreds.email)
    valcreds.send_text(AddUserLocators.password, AddUserCreds.password)
    valcreds.click_button(AddUserLocators.submit_button)

    headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
    headers = [header.text for header in headers_elements]

    assert valcreds.is_url_correct(Env.contact_list)
    assert headers == headers_contact_list
