import pytest

from tests.UI_tests.data_test.constants import StringsPage
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators
from tests.UI_tests.pages.base_page import BasePage

@pytest.mark.navigation
@pytest.mark.test_start_page
class TestStartPage:

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_open_start_page(self, driver, logger):
        osp = BasePage(driver, Env.url, logger)

        assert osp.get_title() == StringsPage.title
        assert osp.get_visibility(StartPageLocators.title) is True

    @pytest.mark.functional
    def test_here_link(self, driver, logger):
        hl = BasePage(driver, Env.url, logger)
        hl.click_button(StartPageLocators.here_link)

        assert hl.is_url_correct(Env.documenter_url)
