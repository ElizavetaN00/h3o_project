import re

from tests.UI_tests.data_test.creds import SimonUserCreds
from tests.UI_tests.data_test.locators import ContactListPageLocators, AddContactPageLocators
from tests.UI_tests.pages.base_page import BasePage


class AddContact(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.log_in(SimonUserCreds.email,
                    SimonUserCreds.password)
        self.click_button(ContactListPageLocators.add_contact_button)


    def enter_new_contact(self, first_name = None, last_name = None, birthdate = None,
                   email = None, phone = None, street1 = None, street2 = None,
                   city = None, state_province = None, postal_code = None, country = None):

        if first_name is not None:
            self.send_text(AddContactPageLocators.first_name, first_name)
        if last_name is not None:
            self.send_text(AddContactPageLocators.last_name, last_name)
        if birthdate is not None:
            self.send_text(AddContactPageLocators.birthdate, birthdate)
        if email is not None:
            self.send_text(AddContactPageLocators.email, email)
        if phone is not None:
            self.send_text(AddContactPageLocators.phone, phone)
        if street1 is not None:
            self.send_text(AddContactPageLocators.street1, street1)
        if street2 is not None:
            self.send_text(AddContactPageLocators.street2, street2)
        if city is not None:
            self.send_text(AddContactPageLocators.city, city)
        if state_province is not None:
            self.send_text(AddContactPageLocators.state_province, state_province)
        if postal_code is not None:
            self.send_text(AddContactPageLocators.postal_code, postal_code)
        if country is not None:
            self.send_text(AddContactPageLocators.country, country)

        self.click_button(AddContactPageLocators.submit_button)


    def table_contact_list(self):
        contact_list = []
        every_cell_info_elements = self.waiting_for_all_elements(ContactListPageLocators.every_cell)
        every_cell_info = [eci.text for eci in every_cell_info_elements]

        for i in range(0, len(every_cell_info), 7):
            contact_list.append(every_cell_info[i : i + 7])

        return contact_list


    @staticmethod
    def convert_to_line(first_name = '', last_name = '', birthdate = '', email = '',
                        phone = '', street1 = '', street2 = '', city = '',
                        state_province = '', postal_code = '', country = ''):

        data = [' '.join((first_name, last_name)), birthdate, email, phone,
                ' '.join((street1, street2)), ' '.join((city, state_province, postal_code)),
                country]

        for i, v in enumerate(data):
            if re.fullmatch(r'\s+', v):
                data[i] = ''
            else:
                data[i] = data[i].strip()

        return data
