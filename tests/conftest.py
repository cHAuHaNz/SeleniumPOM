import pytest
from selenium import webdriver

from config import Configuration


@pytest.fixture()
def setup_and_teardown(request):
    browser = Configuration.read_value('basic', 'browser')
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()
    elif browser == 'brave':
        options = webdriver.ChromeOptions()
        options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
        driver = webdriver.Chrome(options=options)
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        raise Exception(f'Unknown browser: {browser}. Please check config.ini file.')
    request.cls.driver = driver
    driver.get(Configuration.read_value('basic', 'url'))
    yield
    driver.quit()
