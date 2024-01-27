from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from config import Configuration


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = float(Configuration.read_value('basic', 'timeout'))

    def get_element(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def get_interactive_element(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator: tuple[str, str]):
        self.get_interactive_element(locator).click()

    def send_keys_to_element(self, locator: tuple[str, str], keys: str) -> WebElement:
        element = self.get_interactive_element(locator)
        element.clear()
        element.send_keys(keys)
        return element

    def is_element_displayed(self, locator: tuple[str, str]) -> bool:
        return self.get_element(locator).is_displayed()

    def is_element_selected(self, locator: tuple[str, str]):
        return self.get_element(locator).is_selected()

    def get_text_from_element(self, locator: tuple[str, str]) -> str:
        return self.get_element(locator).text
