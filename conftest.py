import pytest
from selenium import webdriver


@pytest.fixture(name='driver')
def fixture_driver():
  browser = webdriver.Firefox()
  yield browser
  browser.quit()
