import logging

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

@pytest.fixture(scope='session')
def logger():
    test_logger = logging.getLogger('test_logger')
    test_logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    test_logger.addHandler(ch)

    return test_logger
