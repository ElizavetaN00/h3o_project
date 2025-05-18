from tests.UI_tests.data_test.constants import StringsPage, ErrorMsg
from tests.UI_tests.data_test.creds import RegistrationUserCreds, SimonUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import RegistrationPageLocators, ContactListPageLocators
from tests.UI_tests.pages.addUser_page import AddUserPage


def test_valid_credentials(driver):

    valcreds = AddUserPage(driver, Env.url)
    valcreds.enter_data(RegistrationUserCreds.first_name,
                        RegistrationUserCreds.last_name,
                        RegistrationUserCreds.email,
                        RegistrationUserCreds.password)
    valcreds.click_button(RegistrationPageLocators.submit_button)

    headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
    headers = [header.text for header in headers_elements]

    assert valcreds.is_url_correct(Env.contact_list_url)
    assert headers == StringsPage.headers_contact_list


def test_empty_first_name(driver):

    empty_fn = AddUserPage(driver, Env.url)
    empty_fn.enter_data('',
                        RegistrationUserCreds.last_name,
                        RegistrationUserCreds.email,
                        RegistrationUserCreds.password
                        )
    empty_fn.click_button(RegistrationPageLocators.submit_button)

    assert (empty_fn.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.first_name_error)


def test_empty_last_name(driver):

    empty_ln = AddUserPage(driver, Env.url)
    empty_ln.enter_data(RegistrationUserCreds.first_name,
                        '',
                        RegistrationUserCreds.email,
                        RegistrationUserCreds.password
                        )
    empty_ln.click_button(RegistrationPageLocators.submit_button)

    assert (empty_ln.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.last_name_error)


def test_empty_email(driver):

    empty_email = AddUserPage(driver, Env.url)
    empty_email.enter_data(RegistrationUserCreds.first_name,
                           RegistrationUserCreds.last_name,
                        '',
                           RegistrationUserCreds.password
                           )
    empty_email.click_button(RegistrationPageLocators.submit_button)

    assert (empty_email.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.email_error)


def test_empty_password(driver):

    empty_password = AddUserPage(driver, Env.url)
    empty_password.enter_data(RegistrationUserCreds.first_name,
                              RegistrationUserCreds.last_name,
                              RegistrationUserCreds.email,
                              ''
                              )
    empty_password.click_button(RegistrationPageLocators.submit_button)

    assert (empty_password.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.password_error)


def test_already_registered_email(driver):

    alreem = AddUserPage(driver, Env.url)
    alreem.enter_data(SimonUserCreds.first_name,
                      SimonUserCreds.last_name,
                      SimonUserCreds.email,
                      SimonUserCreds.password)
    alreem.click_button(RegistrationPageLocators.submit_button)

    assert (alreem.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.alreem_error)


def test_invalid_email_1(driver):

    invalid_email = AddUserPage(driver, Env.url)
    invalid_email.enter_data(RegistrationUserCreds.first_name,
                             RegistrationUserCreds.last_name,
                             RegistrationUserCreds.email[:9] + RegistrationUserCreds.email[10:],
                             RegistrationUserCreds.password)
    invalid_email.click_button(RegistrationPageLocators.submit_button)

    assert (invalid_email.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.email_error)


def test_invalid_email_2(driver):

    invalid_email = AddUserPage(driver, Env.url)
    invalid_email.enter_data(RegistrationUserCreds.first_name,
                             RegistrationUserCreds.last_name,
                             RegistrationUserCreds.email[:10],
                             RegistrationUserCreds.password)
    invalid_email.click_button(RegistrationPageLocators.submit_button)

    assert (invalid_email.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.email_error)


def test_with_spaces_in_email(driver):
    spaces_email = AddUserPage(driver, Env.url)
    spaces_email.enter_data(RegistrationUserCreds.first_name,
                            RegistrationUserCreds.last_name,
                            RegistrationUserCreds.email + '   ',
                            RegistrationUserCreds.password)
    spaces_email.click_button(RegistrationPageLocators.submit_button)

    assert spaces_email.is_url_correct(Env.contact_list_url)


def test_with_uppercase_in_email(driver):
    uppercase_email = AddUserPage(driver, Env.url)
    uppercase_email.enter_data(RegistrationUserCreds.first_name,
                               RegistrationUserCreds.last_name,
                               RegistrationUserCreds.email.upper(),
                               RegistrationUserCreds.password)
    uppercase_email.click_button(RegistrationPageLocators.submit_button)

    assert uppercase_email.is_url_correct(Env.contact_list_url)


def test_with_min_length_fields(driver):
    min_len = AddUserPage(driver, Env.url)
    min_len.enter_data(RegistrationUserCreds.first_name[0],
                       RegistrationUserCreds.last_name[0],
                       RegistrationUserCreds.email,
                       RegistrationUserCreds.password[:7])
    min_len.click_button(RegistrationPageLocators.submit_button)

    assert min_len.is_url_correct(Env.contact_list_url)


def test_with_max_length_fields(driver):
    max_len = AddUserPage(driver, Env.url)
    fn, ln, em, pw = (RegistrationUserCreds.first_name * 5,
                      RegistrationUserCreds.last_name * 5,
                      RegistrationUserCreds.email * 50,
                      RegistrationUserCreds.password * 50)
    max_len.enter_data(fn, ln, em, pw)
    max_len.click_button(RegistrationPageLocators.submit_button)

    assert (max_len.get_error_message
            (RegistrationPageLocators.error_message) == ErrorMsg.max_len_error(fn, ln, pw))


def test_cancel_registration(driver):
    cancel_reg = AddUserPage(driver, Env.url)
    cancel_reg.click_button(RegistrationPageLocators.cancel_button)

    assert cancel_reg.is_url_correct(Env.url)
