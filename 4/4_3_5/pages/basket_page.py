from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Корзина не пуста, но должна была быть"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Сообщение о том, что корзина пуста, не отображается"
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, \
            "Корзина не пуста, сообщение об ошибке"
