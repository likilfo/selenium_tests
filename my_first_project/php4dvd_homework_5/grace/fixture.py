from selenium import webdriver
import pytest
from application import Application


@pytest.fixture(scope='module')
def app(request, browser_type, base_url):
    if browser_type == 'firefox':
        driver = webdriver.Firefox(webdriver.FirefoxProfile("/home/user/.mozilla/firefox/o5ewdhlk.test/"))
    elif browser_type == 'chrome':
        driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)
