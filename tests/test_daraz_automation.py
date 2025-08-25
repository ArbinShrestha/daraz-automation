import pytest
from pages import cart_page
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.driver_setup import get_driver 
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

URL = "https://www.daraz.com.np/"


@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    driver.get(URL)
    yield driver
    driver.quit()


def test_daraz_flow(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.go_to_home()
    login_page.login(EMAIL, PASSWORD)


    search_page = SearchPage(driver)
    search_page.search_product("laptop")
    search_page.filter_by_brand("Apple")
    search_page.click_first_product()

    product_page = ProductPage(driver)
    # product_page.add_to_cart()
    # product_page.navigate_to_cart() 

    cart_page = CartPage(driver)
    initial_cart_count = product_page.get_initial_cart_count()

    # Add item to cart and close popup
    product_page.add_to_cart()

    # Navigate to cart page
    product_page.navigate_to_cart()

    # Get updated cart count
    updated_cart_count = cart_page.get_cart_count()

    # Verify cart count increased by 1
    assert updated_cart_count == initial_cart_count + 1, \
        f"Expected cart count to be {initial_cart_count + 1}, but got {updated_cart_count}"
    print("Success: Cart count increased by 1.")

    # Verify item quantity is 1
    item_quantity = cart_page.get_item_quantity()
    assert item_quantity == 1, f"Expected item quantity to be 1, but got {item_quantity}"
    print("Success: Item quantity is 1.")

