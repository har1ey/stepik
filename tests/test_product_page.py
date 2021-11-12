from pages.product_page import ProductPage
import pytest

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('link', [pytest.param(base_link + str(num), marks=pytest.mark.xfail) if num == 7
                                  else base_link + str(num) for num in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_protuct_to_backet()
