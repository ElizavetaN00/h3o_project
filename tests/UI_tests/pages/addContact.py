from tests.UI_tests.data_test.creds import SimonUserCreds
from tests.UI_tests.data_test.locators import ContactListPageLocators, AddContactPageLocators
from tests.UI_tests.pages.base_page import BasePage


class AddContact(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.log_in(SimonUserCreds.email,
                    SimonUserCreds.password)
        self.click_button(ContactListPageLocators.add_contact_button)


    def enter_data(self,
                   first_name = None,
                   last_name = None,
                   birthdate = None,
                   email = None,
                   phone = None,
                   street1 = None,
                   street2 = None,
                   city = None,
                   state_province = None,
                   postal_code = None,
                   country = None,):

        self.send_text(AddContactPageLocators.first_name, first_name)
        self.send_text(AddContactPageLocators.last_name, last_name)
        self.send_text(AddContactPageLocators.birthdate, birthdate)
        self.send_text(AddContactPageLocators.email, email)
        self.send_text(AddContactPageLocators.phone, phone)
        self.send_text(AddContactPageLocators.street1, street1)
        self.send_text(AddContactPageLocators.street2, street2)
        self.send_text(AddContactPageLocators.city, city)
        self.send_text(AddContactPageLocators.state_province, state_province)
        self.send_text(AddContactPageLocators.postal_code, postal_code)
        self.send_text(AddContactPageLocators.country, country)

        self.click_button(AddContactPageLocators.submit_button)
