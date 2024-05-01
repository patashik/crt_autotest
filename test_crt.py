import pytest
import time
import allure
import json
from selenium import webdriver
from .pages.base_page import BasePage
from .pages.sign_up_page import SignUpPage
from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage


class TestChrome:
    @allure.story("Sign up, log in, log out")
    @allure.sub_suite("Sign up, log in, log out")
    @allure.title("Sign up, log in, log out")
    def test_sign_up_log_in_log_out(self, browser_chrome):
        link = "http://localhost:5000"
        email = str(time.time()) + "@fakemail.org"
        password = "Password01/"
        name = "User"
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: open login page"):
            sign_up_page.should_change_url()
            login_page = LoginPage(browser_chrome, browser_chrome.current_url)
            login_page.should_be_login_page()
        with allure.step("Step 5: log in"):
            login_page.log_in(email, password)
        with allure.step("Step 6: open profile page"):
            login_page.should_change_url()
            profile_page = ProfilePage(browser_chrome, browser_chrome.current_url)
            profile_page.should_be_profile_page(name)
        with allure.step("Step 7: log out"):
            profile_page.log_out()
            profile_page.should_change_url()
            main_page = BasePage(browser_chrome, browser_chrome.current_url)
            main_page.all_elements_on_main_page()

    @allure.story("Log in")
    @allure.sub_suite("Log in")
    @allure.title("Log in with checkbox")
    def test_log_in_with_checkbox(self):
        browser = webdriver.Chrome() 
        link = "http://localhost:5000"
        email = str(time.time()) + "@fakemail.org"
        password = "Password01/"
        name = "User"
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser, browser.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: open login page"):
            sign_up_page.should_change_url()
            login_page = LoginPage(browser, browser.current_url)
            login_page.should_be_login_page()
        with allure.step("Step 5: log in"):
            login_page.log_in_with_checkbox(email, password)
        with allure.step("Step 4: open profile page"):
            login_page.should_change_url()
            profile_page = ProfilePage(browser, browser.current_url)
            profile_page.should_be_profile_page(name)
            cookies = browser.get_cookies()
            with open('cookies.json', 'w') as file:
                json.dump(cookies, file)   
        with allure.step("Step 5: restart browser"):
            profile_page.close()
            browser = webdriver.Chrome()
            main_page = BasePage(browser, link)
            main_page.open()
            with open('cookies.json', 'r') as file:
                cookies = json.load(file)
                for cookie in cookies:
                    browser.add_cookie(cookie)
            browser.refresh()
        with allure.step("Step 6: check if remembered"):
            main_page.all_elements_on_main_page_when_logged_in()
        with allure.step("Step 7: log out"):
            main_page.log_out()
            browser.quit()
    
    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up without name")
    def test_sign_up_no_name(self, browser_chrome):
        link = "http://localhost:5000"
        email = str(time.time()) + "@fakemail.org"
        password = "Password01/"
        name = ""
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: open login page"):
            sign_up_page.should_change_url()
            login_page = LoginPage(browser_chrome, browser_chrome.current_url)
            login_page.should_be_login_page()

    @pytest.mark.nopassword
    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up without password")
    def test_sign_up_no_password(self, browser_chrome):
        link = "http://localhost:5000"
        email = str(time.time()) + "@fakemail.org"
        password = ""
        name = ""
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: should stay on sign up page and show message"):
            sign_up_page.should_be_sign_up_page()
    
    @pytest.mark.noat
    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up without @ in email")
    def test_sign_up_email_without_at(self, browser_chrome):
        link = "http://localhost:5000"
        email = "test"
        password = "Password01/"
        name = ""
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: get error message"):
            sign_up_page.message_email_no_at(email)
        
    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up with email without local part")
    def test_sign_up_email_empty_before_at(self, browser_chrome):
        link = "http://localhost:5000"
        email = "@example.org"
        password = "Password01/"
        name = ""
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: get error message"):
            sign_up_page.message_email_empty_before_at(email)
    
    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up with email without domain part")
    def test_sign_up_email_empty_after_at(self, browser_chrome):
        link = "http://localhost:5000"
        email = "test@"
        password = "Password01/"
        name = ""
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: get error message"):
            sign_up_page.message_email_empty_after_at(email)

    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up with email without double @")
    def test_sign_up_email_double_at(self, browser_chrome):
        link = "http://localhost:5000"
        email = "test@@example.org"
        password = "Password01/"
        name = ""
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 4: get error message"):
            sign_up_page.message_email_double_at()

    @pytest.mark.taken
    @allure.story("Sign up")
    @allure.sub_suite("Sign up")
    @allure.title("Sign up with already taken email")
    def test_sign_up_taken_email(self, browser_chrome):
        link = "http://localhost:5000"
        email = "test@example.org"
        password = "Password01/"
        name = "Test user"
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
            main_page.all_elements_on_main_page()
        with allure.step("Step 2: go to sign up"):
            main_page.go_to_sign_up_page()
            sign_up_page = SignUpPage(browser_chrome, browser_chrome.current_url)
            sign_up_page.should_be_sign_up_page()
        with allure.step("Step 3: fill sign up fields"):
            sign_up_page.sign_up_all_fields(email, password, name)
        with allure.step("Step 3: get error message and go to login page"):
            sign_up_page.message_email_exists()
        with allure.step("Step 5: click login in message"):
            sign_up_page.click_login_in_message()
            login_page = LoginPage(browser_chrome, browser_chrome.current_url)
            login_page.should_be_login_page()

    @allure.story("Resize browser window")
    @allure.sub_suite("Resize browser window")
    @allure.title("Reduce browser window size")
    def test_reduce_window_size(self, browser_chrome):
        link = "http://localhost:5000"
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: maximize window"):
            main_page.maximize_window()
        with allure.step("Step 3: check page elements"):
            main_page.all_elements_on_main_page()
        with allure.step("Step 4: reduce window size"):
            width = 500
            height = 1000
            main_page.resize_window(width, height)
        with allure.step("Step 5: check page elements"):
            main_page.all_elements_on_main_page()
        
        
    
