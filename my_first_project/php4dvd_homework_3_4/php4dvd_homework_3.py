# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from functions import find_element
from functions import open_site
from elements import AddMovie



class TestVideoAdd():
    def test_new_video_required_fields(self, open_site, title='Effie Gray', year='2014'):
        """Добавляет новое видео"""
        self.driver = open_site
        find_element(self.driver, AddMovie.ADD_MOVIE).click()
        find_element(self.driver, AddMovie.TITLE).send_keys(title)
        find_element(self.driver, AddMovie.YEAR).send_keys(year)
        find_element(self.driver, AddMovie.SAVE).click()
        find_element(self.driver, (By.XPATH, '//h2[contains(text(), "%s (%s)")]' % (title, year)))


    def test_new_video_missed_all_required_fields(self, open_site):
        driver = open_site
        find_element(driver, AddMovie.ADD_MOVIE).click()
        find_element(driver, AddMovie.SAVE).click()
        find_element(driver, (By.XPATH, '//*[@name="name"]/following-sibling::*[contains(text(), "This field is required")]'))
        find_element(driver, (By.XPATH, '//*[@name="year"]/following-sibling::*[contains(text(), "This field is required")]'))


    def test_new_video_missed_one_required_fields(self, open_site):
        driver = open_site
        find_element(driver, AddMovie.ADD_MOVIE).click()
        find_element(driver, AddMovie.TITLE).send_keys('Effie Gray')
        find_element(driver, AddMovie.SAVE).click()
        find_element(driver, (By.XPATH, '//*[@name="year"]/following-sibling::*[contains(text(), "This field is required")]'))
