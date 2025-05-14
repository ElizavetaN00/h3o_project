from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import RegistrationPageLocators
from tests.UI_tests.pages.base_page import BasePage


class AddUserPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.first_name_input = RegistrationPageLocators.first_name
        self.last_name_input = RegistrationPageLocators.last_name
        self.email_input = RegistrationPageLocators.email
        self.password_input = RegistrationPageLocators.password
        self.open()
        assert self.is_url_correct(Env.addUser_url)

    def enter_data(self, first_name, last_name, email, password):
        self.send_text(self.first_name_input, first_name)
        self.send_text(self.last_name_input, last_name)
        self.send_text(self.email_input, email)
        self.send_text(self.password_input, password)

    def get_error_message(self):
        error_message = self.waiting_for_all_elements(RegistrationPageLocators.error_message)
        if len(error_message) > 0:
            return error_message[0].text
        return None
