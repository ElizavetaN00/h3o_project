from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from tests.UI_tests.data_test.locators import StartPageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.open()

    def open(self):
        self.driver.get(self.url)

    def click_button(self, locator):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(ec.presence_of_element_located(locator))
        button.click()

    def send_text(self, locator, text):
        wait = WebDriverWait(self.driver, 20)
        input_field = wait.until(ec.presence_of_element_located(locator))
        input_field.send_keys(Keys.CONTROL + 'a')
        input_field.clear()
        input_field.send_keys(text)

    def get_title(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.title_is(self.driver.title))
        return self.driver.title

    def get_visibility(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element.is_displayed()

    def is_url_correct(self, url):
        return self.driver.current_url == url, (f"Expected to get {url} "
                                                f"but got {self.driver.current_url}")

    def waiting_for_all_elements(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(ec.presence_of_all_elements_located(locator))

    def log_in(self, email, password):
        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(ec.presence_of_element_located(StartPageLocators.email))
        password_field = wait.until(ec.presence_of_element_located(StartPageLocators.password))
        submit_button = wait.until(ec.element_to_be_clickable(StartPageLocators.submit_button))

        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.click()

    def get_error_message(self, locator):
        wait = WebDriverWait(self.driver, 10)
        error_message = wait.until(ec.visibility_of_element_located(locator))
        return error_message.text if error_message else None

    def return_text_from_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located(locator))
        return element.text

    def return_text_from_input_field(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located(locator))
        return element.get_attribute('value')
