from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(@href, '/basket/')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_LINK = (By.ID, "login_form")
    REGISTER_LINK = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")


class BasketPageLocators:
    BASKET_FORMSET = (By.ID, "basket_formset")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
