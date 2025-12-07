from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_input.send_keys(password)
        register_button.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception:
            return False
        return True

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Ошибка: 'login' не найдено в URL страницы"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Ошибка: форма логина отсутствует на странице"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Ошибка: форма регистрации отсутствует на странице"
