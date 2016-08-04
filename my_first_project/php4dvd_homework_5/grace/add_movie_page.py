from main_page import MainPage


class AddMovie(MainPage):

    @property
    def fill_title_field(self):
        return self.driver.find_element_by_name('name')

    @property
    def fill_year_field(self):
        return self.driver.find_element_by_name('year')

    @property
    def push_save_button(self):
        return self.driver.find_element_by_id('submit').click()
