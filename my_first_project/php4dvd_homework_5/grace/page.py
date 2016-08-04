from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.common.exceptions import *

class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(visibility_of_element_located(locator))
        except TimeoutException:
            return False
        else:
            return True

    def expected_result(self, locator):
        return self.verify_element_present(locator)
