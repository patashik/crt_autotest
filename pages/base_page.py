from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
import requests


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)

    def close(self):
        self.browser.close()

    def should_be_correct_response_status_code(self):
        code = 200
        try:
            status_code = requests.get(self.browser.current_url).status_code
            assert status_code == code, "HTTP status code not correct"
        except TimeoutException:
            return False
        return True

    def all_header_elements(self):
        assert self.is_clickable(*BasePageLocators.HOME_BUTTON), 'No home button'
        assert self.is_clickable(*BasePageLocators.LOGIN_BUTTON), 'No login button'
        assert self.is_clickable(*BasePageLocators.SIGN_UP_BUTTON), 'No sign up button'
    
    def all_elements_on_main_page(self):
        self.all_header_elements()
        assert self.is_visible(*BasePageLocators.PAGE_TEXT), 'No page title'
        assert self.is_visible(*BasePageLocators.PAGE_TEXT).text == 'Test home page', 'Incorrect page title'
        
    def all_elements_on_main_page_when_logged_in(self):
        assert self.is_clickable(*BasePageLocators.HOME_BUTTON), 'No home button'
        assert self.is_clickable(*BasePageLocators.PROFILE_BUTTON), 'No profile button'
        assert self.is_clickable(*BasePageLocators.LOGOUT_BUTTON),  'No logout button'
        assert self.is_visible(*BasePageLocators.PAGE_TEXT), 'No page title'

    def go_to_sign_up_page(self):
        self.is_clickable(*BasePageLocators.SIGN_UP_BUTTON).click()
        self.should_change_url()

    def go_to_login_page(self):
        self.is_clickable(*BasePageLocators.LOGIN_BUTTON).click()
        self.should_change_url()
    
    def is_clickable(self, how, what, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout, 2).until(
                EC.element_to_be_clickable((how, what))
            )
        except TimeoutException:
            return False
        return element

    def is_visible(self, how, what, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout, 1).until(
                EC.visibility_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return element
               
    def log_out(self):
        self.is_clickable(*BasePageLocators.LOGOUT_BUTTON).click()
    
    def maximize_window(self):
        self.browser.maximize_window()
            
    def resize_window(self, width, height):
        self.browser.set_window_size(width, height)

    def should_change_url(self):
        assert self.url_changes(), "Url did not change"

    def url_changes(self, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.url_changes((self.url))
            )
        except TimeoutException:
            return False
        return True

    def url_contains(self, url_text, timeout=20):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.url_contains(url_text)
            )
        except TimeoutException:
            return False
        return True