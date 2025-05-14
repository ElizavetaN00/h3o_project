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


def test_empty_first_name(driver):
    error_first_name = 'User validation failed: firstName: Path `firstName` is required.'

    empty_fn = AddUserPage(driver, Env.addUser_url)
    empty_fn.enter_data('',
                        AddUserCreds.last_name,
                        AddUserCreds.email,
                        AddUserCreds.password
                        )
    empty_fn.click_button(RegistrationPageLocators.submit_button)

    assert empty_fn.get_error_message() == error_first_name


def test_empty_last_name(driver):
    error_last_name = 'User validation failed: lastName: Path `lastName` is required.'

    empty_fn = AddUserPage(driver, Env.addUser_url)
    empty_fn.enter_data(AddUserCreds.first_name,
                        '',
                        AddUserCreds.email,
                        AddUserCreds.password
                        )
    empty_fn.click_button(RegistrationPageLocators.submit_button)

    assert empty_fn.get_error_message() == error_last_name
