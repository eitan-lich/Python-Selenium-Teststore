from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, '[name="s"]')


class CartPageLocators:
    CHECKOUT_BUTTON = (By.LINK_TEXT, "PROCEED TO CHECKOUT")


class OrderPageLocators:
    SOCIAL_TITLE_MR = (By.CSS_SELECTOR, "[class] .radio-inline:nth-of-type(1) [name]")
    SOCIAL_TITLE_MS = (By.CSS_SELECTOR, "[class] .radio-inline:nth-of-type(2) [name]")
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstname']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL = (By.CSS_SELECTOR, "form#customer-form > section input[name='email']")
    AGREE_TERMS = (By.CSS_SELECTOR, "[name='psgdpr']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "form#customer-form  button[name='continue']")

class ResultPageLocators:
    FIRST_ITEM = (By.LINK_TEXT, "Hummingbird Printed T-Shirt")


class ItemPageLocators:
    ADD_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart.btn.btn-primary")
    CLOSE_POPUP = (By.CSS_SELECTOR, ".close")
    CART_BUTTON = (By.CSS_SELECTOR, "div#_desktop_cart a[rel='nofollow']")