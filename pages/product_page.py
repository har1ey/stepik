from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''

    def add_protuct_to_backet(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_add_button()

        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

        if '?promo=' in self.url:
            self.solve_quiz_and_get_code()

        self.should_be_success()
        self.check_success_message()

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not " \
                                                                                "presented "

    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                                       "basket not found "

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is presented, but should not be"

    def should_not_be_disappearing_message(self):
        assert self.is_dissapeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "The message did not disappear."
