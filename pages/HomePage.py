from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_field = (By.CSS_SELECTOR, '[name="q"]')
        self.search_button = (By.CSS_SELECTOR, '[name="btnK"]')
        self.result_stats = (By.CSS_SELECTOR, '#result-stats')


    def search(self, text: str):
        self.send_keys_to_element(self.search_field, text)
        self.click_element(self.search_button)
