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
