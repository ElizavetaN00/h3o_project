from tests.UI_tests.data_test.constants import ErrorMsg, StringsPage
from tests.UI_tests.data_test.creds import SimonUserCreds, RegistrationUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators, ContactListPageLocators
from tests.UI_tests.pages.base_page import BasePage


def test_valid_credentials(driver):

    valcreds = BasePage(driver, Env.url)
    valcreds.log_in(SimonUserCreds.email,
                    SimonUserCreds.password)

    headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
    headers = [header.text for header in headers_elements]

    assert valcreds.is_url_correct(Env.contact_list_url)
    assert headers == StringsPage.headers_contact_list


def test_empty_form(driver):

    e_form = BasePage(driver, Env.url)
    e_form.click_button(StartPageLocators.submit_button)

    assert e_form.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error


def test_empty_email(driver):

    e_email = BasePage(driver, Env.url)
    e_email.log_in('', SimonUserCreds.password)

    assert e_email.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error


def test_empty_password(driver):

    e_password = BasePage(driver, Env.url)
    e_password.log_in(StartPageLocators.email, '')

    assert e_password.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error


def test_not_registered_email(driver):

    not_reg_email = BasePage(driver, Env.url)
    not_reg_email.log_in(RegistrationUserCreds.email,
                         RegistrationUserCreds.password)

    assert not_reg_email.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error


def test_incorrect_password(driver):

    inc_pass = BasePage(driver, Env.url)
    inc_pass.log_in(SimonUserCreds.email,
                    RegistrationUserCreds.password)

    assert inc_pass.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error
