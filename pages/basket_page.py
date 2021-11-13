from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Basket not empty"

    def should_be_basket_empty_text(self):
        basket_empty_text = self.browser.find_elements(*BasketPageLocators.BASKET_EMPTY_TEXT)[0].text.split('.')[0]
        print(basket_empty_text)
        assert basket_empty_text == 'Your basket is empty', "Empty basket text not found"
