import pytest
from faker import Faker
from faker.providers import internet, misc
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#@pytest.mark.parametrize('link', [pytest.param(base_link + str(num), marks=pytest.mark.xfail) if num == 7
#                                 else base_link + str(num) for num in range(10)])


@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(misc)
        email = fake.email()
        password = fake.password(length=10)

        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page_login = LoginPage(browser, browser.current_url)
        page_login.open()
        page_login.register_new_user(email, password)
        page_login.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_protuct_to_backet()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_protuct_to_backet()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_protuct_to_backet()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_protuct_to_backet()
    page.should_not_be_disappearing_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
    basket_page.should_be_basket_empty_text()
