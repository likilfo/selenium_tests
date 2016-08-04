from selenium.webdriver.common.by import By
from fixture import app
from data import User
from data import Movie

#
def test_new_video_required_fields(app):
    app.login(User.Admin())
    app.click_add_movie_button()
    app.fill_new_video_required_fields(Movie.Movie())
    app.save_new_video()
    new_movie = Movie.Movie()
    assert app.is_expected_result((By.XPATH, '//h2[contains(text(), "%s (%s)")]'
                                   % (new_movie.title, new_movie.year))) is True

#
def test_new_video_missed_all_required_fields(app):
    app.login(User.Admin())
    app.click_add_movie_button()
    app.save_new_video()
    assert app.is_expected_result((By.XPATH, '//*[@name="name"]/following-sibling::*[contains(text(),'
                                             ' "This field is required")]')) is True
    assert app.is_expected_result((By.XPATH, '//*[@name="year"]/following-sibling::*[contains(text(),'
                                             ' "This field is required")]')) is True


def test_new_video_missed_one_required_fields(app):
    app.login(User.Admin())
    app.click_add_movie_button()
    app.fill_title_field(Movie.Movie())
    app.save_new_video()
    assert app.is_expected_result((By.XPATH, '//*[@name="year"]/following-sibling::*[contains(text(),'
                                              ' "This field is required")]')) is True

#
def test_search_existing_video(app):
    app.login(User.Admin())
    app.add_new_video(Movie.Movie())
    app.click_button_Home()
    app.search_movie(Movie.Movie())
    movie = Movie.Movie()
    assert app.is_expected_result((By.XPATH, '//div[@class="title"][contains(text(), "%s")]' %movie.title)) is True


def test_search_no_existing_video(app):
    app.login(User.Admin())
    app.search_movie(Movie.NoMovie())
    assert app.is_expected_result((By.XPATH, '//*[contains(text(), '
                                             '"No movies where found.")]')) is True


def test_delete_movie(app):
    app.login(User.Admin())
    app.add_new_video(Movie.Movie_for_delete())
    app.click_button_Home()
    app.delete_movie(Movie.Movie_for_delete())
    movie = Movie.Movie_for_delete()
    assert app.is_expected_result((By.XPATH, '//div[@class="title"][contains(text(),'
                                             ' "%s")]' %movie.title)) is not True











