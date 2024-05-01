from selenium.webdriver.common.by import By


class BasePageLocators:
    HOME_BUTTON = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[1]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[2]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[3]')
    PAGE_TEXT = (By.XPATH, '//h1')
    PROFILE_BUTTON = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[2]')
    SIGN_UP_BUTTON = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[3]')
    
class SignUpPageLocators:
    LOGIN_LINK_IN_MESSAGE =  (By.XPATH, '/html/body/section/div[2]//a')
    MESSAGE_EMAIL_EXISTS = (By.XPATH, '/html/body/section/div[2]/div/div/div/div')
    SIGN_UP_EMAIL = (By.XPATH, '//form/div[1]/div/input')
    SIGN_UP_NAME = (By.XPATH, '//form/div[2]/div/input')
    SIGN_UP_PASSWORD = (By.XPATH, '//form/div[3]/div/input')
    SIGN_UP_SUBMIT_BUTTON = (By.XPATH, '//button')

class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//form/div[1]/div/input')
    LOGIN_PASSWORD = (By.XPATH, '//form/div[2]/div/input')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button')
    REMEMBER_ME = (By.XPATH, '//label')

class ProfilePageLocators:
    PAGE_TEXT = (By.XPATH, '//h1')


