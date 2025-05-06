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

@dataclasses.dataclass
class AddUserLocators(StartPageLocators):
     first_name = By.XPATH, "//input[@id='firstName']"
     last_name = By.XPATH, "//input[@id='lastName']"
     cancel_button = By.XPATH, "//button[@id='cancel']"


# класс class AddUserLocators(StartPageLocators): можно заменить на:
# @dataclasses.dataclass
# class RegistrationPageLocators(StartPageLocators):
#     first_name = By.XPATH, "//input[@id='firstName']"
#     last_name = By.XPATH, "//input[@id='lastName']"
#     cancel_button = By.XPATH, "//button[@id='cancel']"
#     error_message = By.XPATH, "//div[@id='error']"
# чтобы было понятнее, что это флоу регистрации


@dataclasses.dataclass
class ContactListPageLocators:
    headers = By.XPATH, '//table[@class="contactTable"]//thead//th'
    add_contact_button = By.XPATH, "//button[@id='add-contact']"
    logout_button = By.XPATH, "//button[@id='logout']"

    # table?


@dataclasses.dataclass
class AddContactPageLocators:
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
    submit_button = By.XPATH, "//button[@id='submit']"
    cancel_button = By.XPATH, "//button[@id='cancel']"
    error_message = By.XPATH, "//div[@id='error']"


@dataclasses.dataclass
class ContactDetailsPageLocators:
    first_name = By.XPATH, "//span[@id='firstName']"
    last_name = By.XPATH, "//span[@id='lastName']"
    birthdate = By.XPATH, "//span[@id='birthdate']"
    email = By.XPATH, "//span[@id='email']"
    phone = By.XPATH, "//span[@id='phone']"
    street1 = By.XPATH, "//span[@id='street1']"
    street2 = By.XPATH, "//span[@id='street2']"
    city = By.XPATH, "//span[@id='city']"
    state_province = By.XPATH, "//span[@id='stateProvince']"
    postal_code = By.XPATH, "//span[@id='postalCode']"
    country = By.XPATH, "//span[@id='country']"
    edit_button = By.XPATH, "//button[@id='edit-contact']"
    delete_button = By.XPATH, "//button[@id='delete']"
    return_button = By.XPATH, "//button[@id='return']"

