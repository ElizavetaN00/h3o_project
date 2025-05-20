import pytest

from tests.UI_tests.data_test.constants import StringsPage
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import StartPageLocators
from tests.UI_tests.pages.base_page import BasePage


@pytest.mark.navigation
@pytest.mark.start_page
class TestStartPage:

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.aceptance
    def test_open_start_page(self, driver):
        osp = BasePage(driver, Env.url)

        assert osp.get_title() == StringsPage.title
        assert osp.get_visibility(StartPageLocators.title) is True

    @pytest.mark.functional
    def test_here_link(self, driver):
        hl = BasePage(driver, Env.url)
        hl.click_button(StartPageLocators.here_link)

        assert hl.is_url_correct(Env.documenter_url)
