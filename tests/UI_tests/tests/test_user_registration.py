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

    assert valcreds.is_url_correct(Env.contact_list_url)
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

    empty_ln = AddUserPage(driver, Env.addUser_url)
    empty_ln.enter_data(AddUserCreds.first_name,
                        '',
                        AddUserCreds.email,
                        AddUserCreds.password
                        )
    empty_ln.click_button(RegistrationPageLocators.submit_button)

    assert empty_ln.get_error_message() == error_last_name


def test_empty_email(driver):
    error_email = 'User validation failed: email: Email is invalid'

    empty_email = AddUserPage(driver, Env.addUser_url)
    empty_email.enter_data(AddUserCreds.first_name,
                           AddUserCreds.last_name,
                        '',
                           AddUserCreds.password
                           )
    empty_email.click_button(RegistrationPageLocators.submit_button)

    assert empty_email.get_error_message() == error_email


def test_empty_password(driver):
    error_password = 'User validation failed: password: Path `password` is required.'

    empty_password = AddUserPage(driver, Env.addUser_url)
    empty_password.enter_data(AddUserCreds.first_name,
                              AddUserCreds.last_name,
                              AddUserCreds.email,
                              ''
                              )
    empty_password.click_button(RegistrationPageLocators.submit_button)

    assert empty_password.get_error_message() == error_password


def test_already_registered_email(driver):
    error_alreem = 'Email address is already in use'

    alreem = AddUserPage(driver, Env.addUser_url)
    alreem.enter_data('Simon',
                      'Wilson',
                      'simonw@gmail.com',
                      'Testsimon4')
    alreem.click_button(RegistrationPageLocators.submit_button)

    assert alreem.get_error_message() == error_alreem


def test_invalid_email_1(driver):
    error_invalid_email = 'User validation failed: email: Email is invalid'

    invalid_email = AddUserPage(driver, Env.addUser_url)
    invalid_email.enter_data(AddUserCreds.first_name,
                             AddUserCreds.last_name,
                             AddUserCreds.email[:9] + AddUserCreds.email[10:],
                             AddUserCreds.password)
    invalid_email.click_button(RegistrationPageLocators.submit_button)

    assert invalid_email.get_error_message() == error_invalid_email


def test_invalid_email_2(driver):
    error_invalid_email = 'User validation failed: email: Email is invalid'

    invalid_email = AddUserPage(driver, Env.addUser_url)
    invalid_email.enter_data(AddUserCreds.first_name,
                             AddUserCreds.last_name,
                             AddUserCreds.email[:10],
                             AddUserCreds.password)
    invalid_email.click_button(RegistrationPageLocators.submit_button)

    assert invalid_email.get_error_message() == error_invalid_email


def test_with_spaces_in_email(driver):
    spaces_email = AddUserPage(driver, Env.addUser_url)
    spaces_email.enter_data(AddUserCreds.first_name,
                             AddUserCreds.last_name,
                             AddUserCreds.email + '   ',
                             AddUserCreds.password)
    spaces_email.click_button(RegistrationPageLocators.submit_button)

    assert spaces_email.is_url_correct(Env.contact_list_url)


def test_with_uppercase_in_email(driver):
    uppercase_email = AddUserPage(driver, Env.addUser_url)
    uppercase_email.enter_data(AddUserCreds.first_name,
                               AddUserCreds.last_name,
                               AddUserCreds.email.upper(),
                               AddUserCreds.password)
    uppercase_email.click_button(RegistrationPageLocators.submit_button)

    assert uppercase_email.is_url_correct(Env.contact_list_url)


def test_with_min_length_fields(driver):
    min_len = AddUserPage(driver, Env.addUser_url)
    min_len.enter_data(AddUserCreds.first_name[0],
                       AddUserCreds.last_name[0],
                       AddUserCreds.email,
                       AddUserCreds.password[:7])
    min_len.click_button(RegistrationPageLocators.submit_button)

    assert min_len.is_url_correct(Env.contact_list_url)
