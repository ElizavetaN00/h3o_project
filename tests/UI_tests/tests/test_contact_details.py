import time

import pytest

from tests.UI_tests.data_test.creds import ContactCreds, RegistrationUserCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import ContactDetailsPageLocators, EditContactPageLocators
from tests.UI_tests.pages.contact_details import ContactDetails


@pytest.mark.contact_management
@pytest.mark.test_contact_details
class TestContactDetails:

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_view_contact_details_page(self, driver):

        view_contact_details = ContactDetails(driver, Env.url)
        data = view_contact_details.list_of_input_add_contact(first_name=ContactCreds.alice_contact_info['first_name'],
                                                              last_name=ContactCreds.alice_contact_info['last_name'])
        view_contact_details.enter_new_contact(*data)
        contact_line = view_contact_details.convert_to_line(*data)
        table = view_contact_details.table_contact_list()
        assert contact_line in table

        view_contact_details.click_button(ContactDetails.find_name_in_table(table, contact_line))
        time.sleep(2)
        assert view_contact_details.is_url_correct(Env.contact_list_url)
        assert data == view_contact_details.contact_details_list()

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_return_to_contact_list(self, driver):
        return_to_contact_list = ContactDetails(driver, Env.url)
        data = return_to_contact_list.list_of_input_add_contact(first_name=ContactCreds.alice_contact_info['first_name'],
                                                                last_name=ContactCreds.alice_contact_info['last_name'])
        return_to_contact_list.enter_new_contact(*data)
        contact_line = return_to_contact_list.convert_to_line(*data)
        table = return_to_contact_list.table_contact_list()
        assert contact_line in table

        return_to_contact_list.click_button(ContactDetails.find_name_in_table(table, contact_line))
        return_to_contact_list.click_button(ContactDetailsPageLocators.return_button)

        assert return_to_contact_list.is_url_correct(Env.contact_list_url)

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_edit_contact_mandatory_fields(self, driver):
        edit_contact = ContactDetails(driver, Env.url)
        data = edit_contact.list_of_input_add_contact(first_name=ContactCreds.alice_contact_info['first_name'],
                                                      last_name=ContactCreds.alice_contact_info['last_name'])
        edit_contact.enter_new_contact(*data)
        contact_line = edit_contact.convert_to_line(*data)
        table = edit_contact.table_contact_list()
        assert contact_line in table

        edit_contact.click_button(ContactDetails.find_name_in_table(table, contact_line))
        edit_contact.click_button(ContactDetailsPageLocators.edit_button)
        time.sleep(2)
        edit_contact.send_text(EditContactPageLocators.first_name, RegistrationUserCreds.first_name)
        edit_contact.send_text(EditContactPageLocators.last_name, RegistrationUserCreds.last_name)
        new_data = edit_contact.edit_contact_details_list()
        edit_contact.click_button(ContactDetailsPageLocators.submit_button)
        time.sleep(2)
        contact_details = edit_contact.contact_details_list()

        assert edit_contact.is_url_correct(Env.contact_details_url)
        assert new_data == contact_details
