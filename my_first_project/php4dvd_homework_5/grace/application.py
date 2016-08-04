from page import Page
from login_page import LoginPage
from main_page import MainPage
from add_movie_page import AddMovie
from selenium.webdriver.common.keys import Keys


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        self.page = Page(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.add_movie_page = AddMovie(driver)

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def click_button_Home(self):
        self.main_page.click_homepage_button

    def click_add_movie_button(self):
        self.main_page.click_add_movie_button

    def fill_title_field(self, movie):
        add = self.add_movie_page
        add.fill_title_field.clear()
        add.fill_title_field.send_keys(movie.title)

    def fill_year_field(self, movie):
        add = self.add_movie_page
        add.fill_year_field.clear()
        add.fill_year_field.send_keys(movie.year)

    def fill_new_video_required_fields(self, movie):
        self.fill_title_field(movie)
        self.fill_year_field(movie)

    def save_new_video(self):
        self.add_movie_page.push_save_button

    def add_new_video(self, movie):
        self.click_add_movie_button()
        self.fill_new_video_required_fields(movie)
        self.save_new_video()

    def is_expected_result(self, locator):
        p = self.page
        return p.expected_result(locator)

    def search_movie(self, movie):
        mp = self.main_page
        mp.input_in_search_movie_field.send_keys(movie.title)
        mp.input_in_search_movie_field.send_keys(Keys.ENTER)


    def delete_movie(self, movie):
        self.search_movie(movie)
        self.main_page.select_movie.click()
        self.main_page.delete_movie_button
        self.driver.switch_to.alert.accept()





