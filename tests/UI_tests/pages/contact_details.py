from tests.UI_tests.data_test.locators import (ContactListPageLocators, ContactDetailsPageLocators,
                                               EditContactPageLocators)
from tests.UI_tests.pages.add_contact import AddContact


class ContactDetails(AddContact):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)
        self.logger = logger

    @staticmethod
    def find_name_in_table(table: list, line: list) -> tuple | None:
        if line in table:
            ind = table.index(line) * 7 + 1

            return ContactListPageLocators.name_cells(index=ind)
        return None

    def contact_details_list(self):
        self.logger.info('Getting contact details list')
        return [self.return_text_from_element(ContactDetailsPageLocators.first_name),
                self.return_text_from_element(ContactDetailsPageLocators.last_name),
                self.return_text_from_element(ContactDetailsPageLocators.birthdate),
                self.return_text_from_element(ContactDetailsPageLocators.email),
                self.return_text_from_element(ContactDetailsPageLocators.phone),
                self.return_text_from_element(ContactDetailsPageLocators.street1),
                self.return_text_from_element(ContactDetailsPageLocators.street2),
                self.return_text_from_element(ContactDetailsPageLocators.city),
                self.return_text_from_element(ContactDetailsPageLocators.state_province),
                self.return_text_from_element(ContactDetailsPageLocators.postal_code),
                self.return_text_from_element(ContactDetailsPageLocators.country)]

    @staticmethod
    def list_of_input_add_contact(first_name = None, last_name = None, birthdate = None,
                   email = None, phone = None, street1 = None, street2 = None,
                   city = None, state_province = None, postal_code = None, country = None):

        return [first_name if first_name is not None else '',
                last_name if last_name is not None else '',
                birthdate if birthdate is not None else '',
                email if email is not None else '',
                phone if phone is not None else '',
                street1 if street1 is not None else '',
                street2 if street2 is not None else '',
                city if city is not None else '',
                state_province if state_province is not None else '',
                postal_code if postal_code is not None else '',
                country if country is not None else '']

    def edit_contact_details_list(self):
        self.logger.info('Getting edit contact details list')
        return [self.return_text_from_input_field(EditContactPageLocators.first_name),
                self.return_text_from_input_field(EditContactPageLocators.last_name),
                self.return_text_from_input_field(EditContactPageLocators.birthdate),
                self.return_text_from_input_field(EditContactPageLocators.email),
                self.return_text_from_input_field(EditContactPageLocators.phone),
                self.return_text_from_input_field(EditContactPageLocators.street1),
                self.return_text_from_input_field(EditContactPageLocators.street2),
                self.return_text_from_input_field(EditContactPageLocators.city),
                self.return_text_from_input_field(EditContactPageLocators.state_province),
                self.return_text_from_input_field(EditContactPageLocators.postal_code),
                self.return_text_from_input_field(EditContactPageLocators.country)]
