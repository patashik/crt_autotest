from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
        def should_be_login_page(self):
            assert self.url_contains('login'), "Not a login page"
            self.all_elements_on_login_page()

        def all_elements_on_login_page(self):
            self.all_header_elements()
            assert self.is_clickable(*LoginPageLocators.LOGIN_EMAIL), 'No email form'
            assert self.is_clickable(*LoginPageLocators.LOGIN_PASSWORD), 'No password form'
            assert self.is_clickable(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), 'No login submit button'
            assert self.is_clickable(*LoginPageLocators.REMEMBER_ME), 'No checkbox'

        def log_in(self, email, password):
            self.is_clickable(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
            self.is_clickable(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
            self.is_clickable(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        def log_in_with_checkbox(self, email, password):
            self.is_clickable(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
            self.is_clickable(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
            self.is_clickable(*LoginPageLocators.REMEMBER_ME).click()
            self.is_clickable(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()