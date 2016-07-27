from selenium.webdriver.common.by import By


class AuthPage():
    """Authentication page element's locators"""
    LOGIN = By.ID, 'username'
    PASSWORD = By.NAME, 'password'
    SUBMIT_BUTTON = By.NAME, 'submit'


class MainPage(AuthPage):
    HOME_BUTTON = By.LINK_TEXT, 'Home'
    ADD_MOVIE = By.XPATH, '//img[@title="Add movie"]'
    SEARCH_MOVIE = By.ID, 'q'


class AddMovie(MainPage):
    SEARCH_FIELD = By.XPATH, './/*[@id="imdbsearch"]'
    SEARCH_BUTTON = By.XPATH, '//*[@id="imdbsearchform"]//input[@type="submit"]'
    TITLE = By.NAME, 'name'
    YEAR = By.NAME, 'year'
    SAVE = By.ID, 'submit'


