import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest
import time

params = list(map(str, range(10)))


@pytest.mark.auth_user
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        page = LoginPage(browser, link)
        page.open()
        email, password = page.make_email_and_pass()
        page.register_new_user(email, password)
        page.should_be_authorized_user()


@pytest.mark.need_review
@pytest.mark.parametrize('param', [
    x if x != '7' else pytest.param(x, marks=pytest.mark.xfail) for x in params])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_click_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


@pytest.mark.need_review
@pytest.mark.xfail(reason="Success message is presented")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_click_cart()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.xfail(reason="Success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_click_cart()
    page.should_be_disappeared_success_message()
