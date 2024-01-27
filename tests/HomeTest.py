from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestHome(BaseTest):

    def test_search(self):
        homepage = HomePage(self.driver)
        homepage.search('selenium')
        assert not homepage.is_element_displayed(homepage.result_stats)
