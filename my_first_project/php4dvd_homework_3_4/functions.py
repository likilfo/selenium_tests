# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import *
# from selenium.common.exceptions import *
# from elements import AuthPage
import pytest


# def find_element(driver, element_locator):
#     """Search element and wait for it become enable."""
#     try:
#         WebDriverWait(driver, 10).until(element_to_be_clickable(element_locator))
#     except TimeoutException:
#         raise Exception('Unable to find text in this element after waiting 10 seconds')
#     else:
#         element = driver.find_element(*element_locator)
#         return element
#
#
# @pytest.fixture()
# def open_site(request):
#     """Prepare enviroment for test execution"""
#     driver = webdriver.Firefox(webdriver.FirefoxProfile("/home/user/.mozilla/firefox/o5ewdhlk.test/"))
#      #driver.maximize_window()
#     driver.get("http://localhost/php4dvd/")
#     find_element(driver, AuthPage.LOGIN).send_keys("admin")
#     find_element(driver, AuthPage.PASSWORD).send_keys('admin')
#     find_element(driver, AuthPage.SUBMIT_BUTTON).click()
#     def close_site():
#          pass
#     #driver.quit()
#     request.addfinalizer(close_site)
#     return driver