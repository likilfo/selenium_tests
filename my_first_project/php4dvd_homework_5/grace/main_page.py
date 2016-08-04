from login_page import LoginPage


class MainPage(LoginPage):

    @property
    def click_homepage_button(self):
        self.driver.find_element_by_link_text("Home").click()

    @property
    def click_add_movie_button(self):
        self.driver.find_element_by_xpath('//img[@title="Add movie"]').click()

    @property
    def input_in_search_movie_field(self):
        return self.driver.find_element_by_id('q')

    @property
    def select_movie(self):
        return self.driver.find_element_by_xpath('//div[@class="title"][contains(text(),"BoringMovie")]')

    @property
    def delete_movie_button(self):
        self.driver.find_element_by_xpath('//img[@title="Remove"]').click
