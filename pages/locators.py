from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FIELD = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDR_INPUT = (By.ID, "id_registration-email")
    PASSWORD1_INPUT = (By.ID, "id_registration-password1")
    PASSWORD2_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")


class CartPageLocators():
    BASKET_EMPTY = (By.ID, "content_inner")
    BASKET_NOT_EMPTY = (By.CLASS_NAME, "basket-title")
    SUBSTRING_BASKET_EN_GB = "Your basket is empty" #"Ваша корзина пуста"
    SUBSTRING_BASKET_RU = "Ваша корзина пуста"