from .base_page import BasePage
from .locators import LoginPageLocators
import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.password = None
        self.email = None

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in str(self.browser.current_url), "Wrong page opened in browser"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "Login field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FIELD), "Register field is not presented"

    def make_email_and_pass(self):
        return (str(time.time()) + "@fakemail.org", "myStrongPassword№121")

    def register_new_user(self, email, password):
        self.email = email
        self.password = password

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDR_INPUT)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)
        reg_button.click()