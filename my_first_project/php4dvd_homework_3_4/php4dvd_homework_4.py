# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from functions import find_element
from functions import open_site
from elements import MainPage
import php4dvd_homework_3



class TestVideoSearch():
   def test_search_existing_video(self, open_site):
       #Перед запуском теста на удаление добавляем фильм, используя тест на добавление
       driver = open_site
       real_movie = 'Matrix'
       my_test = php4dvd_homework_3.TestVideoAdd()
       my_test.test_new_video_required_fields(driver, title=real_movie, year='1999')
       find_element(driver, MainPage.HOME_BUTTON).click()
       find_element(driver, MainPage.SEARCH_MOVIE).send_keys(real_movie)
       find_element(driver, MainPage.SEARCH_MOVIE).send_keys(Keys.ENTER)
       find_element(driver, (By.XPATH, '//div[@class="title"][contains(text(), %s)]' %real_movie))


   def test_search_no_existing_video(self, open_site):
       #Перед запуском теста на удаление добавляем фильм, используя тест на добавление
       driver = open_site
       unreal_movie = u'Груз 200'
       find_element(driver, MainPage.SEARCH_MOVIE).send_keys(unreal_movie)
       find_element(driver, MainPage.SEARCH_MOVIE).send_keys(Keys.ENTER)
       find_element(driver, (By.XPATH, '//*[contains(text(), "No movies where found.")]'))








