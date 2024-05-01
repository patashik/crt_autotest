from .base_page import BasePage
from .locators import SignUpPageLocators

class SignUpPage(BasePage):
    def all_elements_on_sign_up_page(self):
        self.all_header_elements()
        assert self.is_clickable(*SignUpPageLocators.SIGN_UP_EMAIL), 'No email form'
        assert self.is_clickable(*SignUpPageLocators.SIGN_UP_PASSWORD), 'No password form'
        assert self.is_clickable(*SignUpPageLocators.SIGN_UP_SUBMIT_BUTTON), 'No login submit button'
        assert self.is_clickable(*SignUpPageLocators.SIGN_UP_NAME), 'No name form'
    
    def click_login_in_message(self):    
        self.is_clickable(*SignUpPageLocators.LOGIN_LINK_IN_MESSAGE).click()
        self.should_change_url()

    def should_be_sign_up_page(self):
        assert self.url_contains('signup'), "Not a sign up page"
        self.all_elements_on_sign_up_page()

    def sign_up_all_fields(self, email, password, name):
        sign_up_email = self.is_clickable(*SignUpPageLocators.SIGN_UP_EMAIL)
        sign_up_email.send_keys(email)
        sign_up_name = self.is_clickable(*SignUpPageLocators.SIGN_UP_NAME)
        sign_up_name.send_keys(name)
        sign_up_password = self.is_clickable(*SignUpPageLocators.SIGN_UP_PASSWORD)
        sign_up_password.send_keys(password)
        sign_up_submit_button = self.is_clickable(*SignUpPageLocators.SIGN_UP_SUBMIT_BUTTON)
        sign_up_submit_button.click()
    
    def message_email_exists(self):
        self.should_be_sign_up_page()
        assert self.is_visible(*SignUpPageLocators.MESSAGE_EMAIL_EXISTS), "No error message"
        
    def message_email_no_at(self, email):           
        element = self.browser.switch_to.active_element
        assert element.get_attribute('validationMessage') == f'Адрес электронной почты должен содержать символ "@". В адресе "{email}" отсутствует символ "@".'    
    
    def message_email_empty_before_at(self, email):           
        element = self.browser.switch_to.active_element
        assert element.get_attribute('validationMessage') == f'Введите часть адреса до символа "@". Адрес "{email}" неполный.'
    
    def message_email_empty_after_at(self, email):           
        element = self.browser.switch_to.active_element
        assert element.get_attribute('validationMessage') == f'Введите часть адреса после символа "@". Адрес "{email}" неполный.'

    def message_email_double_at(self):           
        element = self.browser.switch_to.active_element
        assert element.get_attribute('validationMessage') == f'Часть адреса после символа "@" не должна содержать символ "@".'

