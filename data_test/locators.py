import dataclasses

from selenium.webdriver.common.by import By


@dataclasses.dataclass
class StartPageLocators:
    title = By.XPATH, '//h1'
    here_link = By.XPATH, '//div//a'
    email = By.XPATH, "//input[@id='email']"
    password = By.XPATH, "//input[@id='password']"
    submit_button = By.XPATH, "//button[@id='submit']"
    sing_up_button = By.XPATH, "//button[@id='signup']"


@dataclasses.dataclass
class AddUserLocators(StartPageLocators):
    first_name = By.XPATH, "//input[@id='firstName']"
    last_name = By.XPATH, "//input[@id='lastName']"
    cancel_button = By.XPATH, "//button[@id='cancel']"


@dataclasses.dataclass
class ContactListLocators:
    headers = By.XPATH, '//table[@class="contactTable"]//thead//th'
