import pytest

from tests.UI_tests.data_test.constants import StringsPage, ErrorMsg
from tests.UI_tests.data_test.creds import RegistrationUserCreds, SimonUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import RegistrationPageLocators, ContactListPageLocators
from tests.UI_tests.pages.add_user_page import AddUserPage

@pytest.mark.test_user_registration
@pytest.mark.authentication
class TestUserRegistration:

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.aceptance
    def test_valid_credentials(self, driver, logger):
        valcreds = AddUserPage(driver, Env.url, logger)
        valcreds.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name,
                                              RegistrationUserCreds.email, RegistrationUserCreds.password)
        valcreds.click_button(RegistrationPageLocators.submit_button)

        headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
        headers = [header.text for header in headers_elements]

        assert valcreds.is_url_correct(Env.contact_list_url)
        assert headers == StringsPage.headers_contact_list

    @pytest.mark.regression
    def test_empty_first_name(self, driver, logger):
        empty_fn = AddUserPage(driver, Env.url, logger)
        empty_fn.enter_data_user_registration('', RegistrationUserCreds.last_name, RegistrationUserCreds.email,
                                              RegistrationUserCreds.password)
        empty_fn.click_button(RegistrationPageLocators.submit_button)

        assert (empty_fn.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.first_name_error)

    @pytest.mark.regression
    def test_empty_last_name(self, driver, logger):
        empty_ln = AddUserPage(driver, Env.url, logger)
        empty_ln.enter_data_user_registration(RegistrationUserCreds.first_name, '', RegistrationUserCreds.email,
                                              RegistrationUserCreds.password)
        empty_ln.click_button(RegistrationPageLocators.submit_button)

        assert (empty_ln.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.last_name_error)

    @pytest.mark.regression
    def test_empty_email(self, driver, logger):
        empty_email = AddUserPage(driver, Env.url, logger)
        empty_email.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name, '',
                                                 RegistrationUserCreds.password)
        empty_email.click_button(RegistrationPageLocators.submit_button)

        assert (empty_email.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.email_error)

    @pytest.mark.regression
    def test_empty_password(self, driver, logger):
        empty_password = AddUserPage(driver, Env.url, logger)
        empty_password.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name,
                                                    RegistrationUserCreds.email, '')
        empty_password.click_button(RegistrationPageLocators.submit_button)

        assert (empty_password.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.password_error)

    @pytest.mark.regression
    def test_already_registered_email(self, driver, logger):
        alreem = AddUserPage(driver, Env.url, logger)
        alreem.enter_data_user_registration(SimonUserCreds.first_name, SimonUserCreds.last_name, SimonUserCreds.email,
                                            SimonUserCreds.password)
        alreem.click_button(RegistrationPageLocators.submit_button)

        assert (alreem.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.alreem_error)

    @pytest.mark.regression
    def test_invalid_email_1(self, driver, logger):
        invalid_email = AddUserPage(driver, Env.url, logger)
        invalid_email.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name,
                                                   RegistrationUserCreds.email[:9] + RegistrationUserCreds.email[10:],
                                                   RegistrationUserCreds.password)
        invalid_email.click_button(RegistrationPageLocators.submit_button)

        assert (invalid_email.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.email_error)

    @pytest.mark.regression
    def test_invalid_email_2(self, driver, logger):
        invalid_email = AddUserPage(driver, Env.url, logger)
        invalid_email.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name,
                                                   RegistrationUserCreds.email[:10], RegistrationUserCreds.password)
        invalid_email.click_button(RegistrationPageLocators.submit_button)

        assert (invalid_email.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.email_error)

    @pytest.mark.regression
    def test_with_spaces_in_email(self, driver, logger):
        spaces_email = AddUserPage(driver, Env.url, logger)
        spaces_email.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name,
                                                  RegistrationUserCreds.email + '   ', RegistrationUserCreds.password)
        spaces_email.click_button(RegistrationPageLocators.submit_button)

        assert spaces_email.is_url_correct(Env.contact_list_url)

    @pytest.mark.regression
    def test_with_uppercase_in_email(self, driver, logger):
        uppercase_email = AddUserPage(driver, Env.url, logger)
        uppercase_email.enter_data_user_registration(RegistrationUserCreds.first_name, RegistrationUserCreds.last_name,
                                                     RegistrationUserCreds.email.upper(),
                                                     RegistrationUserCreds.password)
        uppercase_email.click_button(RegistrationPageLocators.submit_button)

        assert uppercase_email.is_url_correct(Env.contact_list_url)

    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_with_min_length_fields(self, driver, logger):
        min_len = AddUserPage(driver, Env.url, logger)
        min_len.enter_data_user_registration(RegistrationUserCreds.first_name[0], RegistrationUserCreds.last_name[0],
                                             RegistrationUserCreds.email, RegistrationUserCreds.password[:7])
        min_len.click_button(RegistrationPageLocators.submit_button)

        assert min_len.is_url_correct(Env.contact_list_url)

    @pytest.mark.acceptance
    def test_with_max_length_fields(self, driver, logger):
        max_len = AddUserPage(driver, Env.url, logger)
        fn, ln, em, pw = (RegistrationUserCreds.first_name * 5,
                          RegistrationUserCreds.last_name * 5,
                          RegistrationUserCreds.email * 50,
                          RegistrationUserCreds.password * 50)
        max_len.enter_data_user_registration(fn, ln, em, pw)
        max_len.click_button(RegistrationPageLocators.submit_button)

        assert (max_len.get_error_message
                (RegistrationPageLocators.error_message) == ErrorMsg.max_len_error(fn, ln, pw))

    @pytest.mark.acceptance
    def test_cancel_registration(self, driver, logger):
        cancel_reg = AddUserPage(driver, Env.url, logger)
        cancel_reg.click_button(RegistrationPageLocators.cancel_button)

        assert cancel_reg.is_url_correct(Env.url)
