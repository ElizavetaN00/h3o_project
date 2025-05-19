import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(name='driver')
def fixture_driver():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
