from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def send_text(self, locator, text):
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_visibility(self, locator):
        input_field = self.driver.find_element(*locator)
        return input_field.is_displayed()

    def is_url_correct(self, url):
        return self.driver.current_url == url, (f"Expected to get {url} "
                                                f"but got {self.driver.current_url}")

    def waiting_for_all_elements(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_all_elements_located(locator))
