from tests.UI_tests.data_test.creds import SimonUserCreds, RegistrationUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators, ContactListPageLocators
from tests.UI_tests.pages.base_page import BasePage


def test_valid_credentials(driver):
    headers_contact_list = ["Name", "Birthdate", "Email", "Phone", "Address",
                            "City, State/Province, Postal Code", "Country"]

    valcreds = BasePage(driver, Env.url)
    valcreds.log_in(SimonUserCreds.email,
                    SimonUserCreds.password)

    headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
    headers = [header.text for header in headers_elements]

    assert valcreds.is_url_correct(Env.contact_list_url)
    assert headers == headers_contact_list


def test_empty_form(driver):
    error_msg = "Incorrect username or password"

    e_form = BasePage(driver, Env.url)
    e_form.click_button(StartPageLocators.submit_button)

    assert e_form.get_error_message(StartPageLocators.error_message) == error_msg


def test_empty_email(driver):
    error_msg = 'Incorrect username or password'

    e_email = BasePage(driver, Env.url)
    e_email.log_in('', SimonUserCreds.password)

    assert e_email.get_error_message(StartPageLocators.error_message) == error_msg


def test_empty_password(driver):
    error_msg = 'Incorrect username or password'

    e_password = BasePage(driver, Env.url)
    e_password.log_in(StartPageLocators.email, '')

    assert e_password.get_error_message(StartPageLocators.error_message) == error_msg


def test_not_registered_email(driver):
    error_msg = 'Incorrect username or password'

    not_reg_email = BasePage(driver, Env.url)
    not_reg_email.log_in(RegistrationUserCreds.email,
                         RegistrationUserCreds.password)

    assert not_reg_email.get_error_message(StartPageLocators.error_message) == error_msg
