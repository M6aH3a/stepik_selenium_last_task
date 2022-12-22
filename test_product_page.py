import pytest
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time

params = list(map(str, range(10)))


@pytest.mark.parametrize('param', [
    x if x != '7' else pytest.param(x, marks=pytest.mark.xfail) for x in params
])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_click_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
