from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def should_be_profile_page(self, name):
        assert self.url_contains('profile'), "Profile page did not open"
        self.all_elements_on_main_page_when_logged_in()
        assert self.is_visible(*ProfilePageLocators.PAGE_TEXT).text == f'Welcome, {name}!', 'Incorrect welcome message'