from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_count = (By.CLASS_NAME, "cart-num")
        self.item_quantity = (By.CLASS_NAME, "item-quantity-value")

    def get_cart_count(self):
        # Retrieve the current cart count.
        try:
            cart_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.cart_count)
            )
            raw_text = cart_icon.text
            cart_count = int(raw_text) if raw_text.isdigit() else 0
            return cart_count
        except Exception as e:
            print(f"Error retrieving cart count: {e}")
            return 0

    def get_item_quantity(self):
        # Retrieve the quantity of the first item in the cart.
        try:
            quantity_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.item_quantity)
            )
            raw_text = quantity_element.text
            quantity = int(raw_text) if raw_text.isdigit() else 0
            return quantity
        except Exception as e:
            print(f"Error retrieving item quantity: {e}")
            return 0