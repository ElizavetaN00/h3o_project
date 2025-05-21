import dataclasses
from selenium.webdriver.common.by import By


@dataclasses.dataclass
class StartPageLocators:
    title = By.XPATH, '//h1'
    here_link = By.XPATH, '//div//a'
    email = By.XPATH, "//input[@id='email']"
    password = By.XPATH, "//input[@id='password']"
    submit_button = By.XPATH, "//button[@id='submit']"
    sign_up_button = By.XPATH, "//button[@id='signup']"
    error_message = By.XPATH, "//span[@id='error']"
    main_page_content = By.XPATH, '//div[@class="main-content"]'


@dataclasses.dataclass
class RegistrationPageLocators(StartPageLocators):
    first_name = By.XPATH, "//input[@id='firstName']"
    last_name = By.XPATH, "//input[@id='lastName']"
    cancel_button = By.XPATH, "//button[@id='cancel']"
    log_out_button = By.XPATH, "//button[@id='logout']"


@dataclasses.dataclass
class ContactListPageLocators:
    headers = By.XPATH, '//table[@class="contactTable"]//thead//th'
    add_contact_button = By.XPATH, "//button[@id='add-contact']"
    logout_button = By.XPATH, "//button[@id='logout']"
    line_contact = By.XPATH, '//tr[@class="contactTableBodyRow"]'
    every_cell = By.XPATH, '(//td[not(@hidden="true")])'

    @staticmethod
    def name_cells(index: int) -> tuple[str, str]:
        return By.XPATH, f'(//td[not(@hidden="true")])[{index}]'



@dataclasses.dataclass
class AddContactPageLocators:
    first_name = By.ID, "firstName"
    last_name = By.ID, "lastName"
    birthdate = By.ID, "birthdate"
    email = By.ID, "email"
    phone = By.ID, "phone"
    street1 = By.ID, "street1"
    street2 = By.ID, "street2"
    city = By.ID, "city"
    state_province = By.ID, "stateProvince"
    postal_code = By.ID, "postalCode"
    country = By.ID, "country"
    submit_button = By.ID, "submit"
    cancel_button = By.ID, "cancel"
    error_message = By.ID, "error"


@dataclasses.dataclass
class ContactDetailsPageLocators(AddContactPageLocators):
    edit_button = By.XPATH, "//button[@id='edit-contact']"
    delete_button = By.XPATH, "//button[@id='delete']"
    return_button = By.XPATH, "//button[@id='return']"

@dataclasses.dataclass
class EditContactPageLocators:
    first_name = By.XPATH, "//input[@id='firstName']"
    last_name = By.XPATH, "//input[@id='lastName']"
    birthdate = By.XPATH, "//input[@id='birthdate']"
    email = By.XPATH, "//input[@id='email']"
    phone = By.XPATH, "//input[@id='phone']"
    street1 = By.XPATH, "//input[@id='street1']"
    street2 = By.XPATH, "//input[@id='street2']"
    city = By.XPATH, "//input[@id='city']"
    state_province = By.XPATH, "//input[@id='stateProvince']"
    postal_code = By.XPATH, "//input[@id='postalCode']"
    country = By.XPATH, "//input[@id='country']"
