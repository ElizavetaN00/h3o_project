import pytest

from tests.UI_tests.data_test.constants import ErrorMsg, StringsPage
from tests.UI_tests.data_test.creds import SimonUserCreds, RegistrationUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators, ContactListPageLocators
from tests.UI_tests.pages.base_page import BasePage

@pytest.mark.test_user_login
@pytest.mark.authentication
class TestUserLogin:

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.aceptance
    def test_valid_credentials(self, driver, logger):
        valcreds = BasePage(driver, Env.url, logger)
        valcreds.log_in(SimonUserCreds.email, SimonUserCreds.password)
        headers_elements = valcreds.waiting_for_all_elements(ContactListPageLocators.headers)
        headers = [header.text for header in headers_elements]
        assert valcreds.is_url_correct(Env.contact_list_url)
        assert headers == StringsPage.headers_contact_list

    @pytest.mark.critical_path
    def test_empty_form(self, driver, logger):
        e_form = BasePage(driver, Env.url, logger)
        e_form.click_button(StartPageLocators.submit_button)

        assert e_form.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error

    @pytest.mark.regression
    def test_empty_email(self, driver, logger):
        e_email = BasePage(driver, Env.url, logger)
        e_email.log_in('', SimonUserCreds.password)

        assert e_email.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error

    @pytest.mark.regression
    def test_empty_password(self, driver, logger):
        e_password = BasePage(driver, Env.url, logger)
        e_password.log_in(StartPageLocators.email, '')
        assert (e_password.get_error_message
                (StartPageLocators.error_message) == ErrorMsg.log_in_error)

    @pytest.mark.regression
    def test_not_registered_email(self, driver, logger):
        not_reg_email = BasePage(driver, Env.url, logger)
        not_reg_email.log_in(RegistrationUserCreds.email, RegistrationUserCreds.password)
        assert (not_reg_email.get_error_message
                (StartPageLocators.error_message) == ErrorMsg.log_in_error)

    @pytest.mark.regression
    def test_incorrect_password(self, driver, logger):
        inc_pass = BasePage(driver, Env.url, logger)
        inc_pass.log_in(SimonUserCreds.email, RegistrationUserCreds.password)
        assert (inc_pass.get_error_message
                (StartPageLocators.error_message) == ErrorMsg.log_in_error)

    @pytest.mark.regression
    def test_no_dog_email(self, driver, logger):
        no_dog = BasePage(driver, Env.url, logger)
        no_dog.log_in(SimonUserCreds.email[:6] + SimonUserCreds.email[7:], SimonUserCreds.password)
        assert no_dog.get_error_message(StartPageLocators.error_message) == ErrorMsg.log_in_error

    @pytest.mark.regression
    def test_spaces_in_email(self, driver, logger):
        spaces_em = BasePage(driver, Env.url, logger)
        spaces_em.log_in(SimonUserCreds.email + ' ' * 3, SimonUserCreds.password)
        assert spaces_em.is_url_correct(Env.addUser_url)

    @pytest.mark.regression
    def test_uppercase_email(self, driver, logger):
        spaces_em = BasePage(driver, Env.url, logger)
        spaces_em.log_in(SimonUserCreds.email.upper(), SimonUserCreds.password)
        assert spaces_em.is_url_correct(Env.addUser_url)

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.aceptance
    def test_log_out(self, driver, logger):
        log_out = BasePage(driver, Env.url, logger)
        log_out.log_in(SimonUserCreds.email, SimonUserCreds.password)
        log_out.click_button(ContactListPageLocators.logout_button)
        assert log_out.is_url_correct(Env.url)
