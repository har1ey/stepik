from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_ = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_.send_keys(email)
        password_ = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password_.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password_confirm.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This URL does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_LINK), "Register form is not presented"
