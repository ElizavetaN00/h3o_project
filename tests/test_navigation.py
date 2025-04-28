from selenium.webdriver.common.by import By

from data_test.env import Env
from pages.base_page import BasePage


def test_open_start_page(driver):
    osp = BasePage(driver, Env.url)
    osp.open()
    title = 'Contact List App'
    title_locator = By.XPATH, '//h1'

    assert osp.get_title() == title
    assert osp.get_visibility(title_locator) is True


def test_here_link(driver):
    hl = BasePage(driver, Env.url)
    hl.open()
    here_link_locator = By.XPATH, '//div//a'
    hl.click_button(here_link_locator)

    assert hl.is_url_correct(Env.documenter)
