import pytest
from selene import browser





@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = ('https://piter-online.net')
    browser.config.window_width = 1920
    browser.config.window_height = 1080


    yield

    browser.quit()