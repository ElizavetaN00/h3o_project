from tests.UI_tests.data_test.creds import AddUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import RegistrationPageLocators, ContactListPageLocators
from tests.UI_tests.pages.addUser_page import AddUserPage


def test_valid_credentials(driver):
    headers_contact_list = ["Name", "Birthdate", "Email", "Phone", "Address",
                            "City, State/Province, Postal Code", "Country"]

    valcreds = AddUserPage(driver, Env.addUser_url)
    valcreds.enter_data(AddUserCreds.first_name,
                        AddUserCreds.last_name,
                        AddUserCreds.email,
                        AddUserCreds.password)
    valcreds.click_button(RegistrationPageLocators.submit_button)

    headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
    headers = [header.text for header in headers_elements]

    assert valcreds.is_url_correct(Env.contact_list)
    assert headers == headers_contact_list
