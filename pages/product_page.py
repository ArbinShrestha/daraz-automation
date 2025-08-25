from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.XPATH, "//button[contains(@class, 'add-to-cart-buy-now-btn') and .//span[text()='Add to Cart']]")
        self.close_popup_button = (By.XPATH, "//a[contains(@class, 'next-dialog-close')]//i[contains(@class, 'next-icon-close')]")
        self.cart_count = (By.ID, "topActionCartNumber")
        self.cart_page_url = "https://cart.daraz.com.np/cart"

    def get_initial_cart_count(self):
        # Retrieve the initial cart count before adding an item.
        try:
            cart_count_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.cart_count))
            cart_count = int(cart_count_element.text) if cart_count_element.text.isdigit() else 0
            print(f"Initial cart count: {cart_count}")
            return cart_count
        except Exception as e:
            print(f"Error retrieving initial cart count: {e}")
            return 0
        
    def add_to_cart(self):
        # Click the 'Add to Cart' button and close the popup. 
        try:
            # Wait for the Add to Cart button to be clickable
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_to_cart_button)
            )
            # Scroll to the button to ensure it's in view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
            add_to_cart_button.click()
            print("Clicked 'Add to Cart' button.")

            # Wait for cart count to update (optional, to ensure item is added)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.cart_count)
            )
            print("Cart count element detected after adding item.")

            # Wait for the popup to appear and close it
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.close_popup_button)
            )
            close_button.click()
            print("Closed the popup.")
        except Exception as e:
            print(f"Error during add to cart or closing popup: {e}")
        time.sleep(2)

    def navigate_to_cart(self):
        # Navigate to the cart page.
        try:
            self.driver.get(self.cart_page_url)
            print(f"Navigated to cart page: {self.cart_page_url}")
        except Exception as e:
            print(f"Error navigating to cart page: {e}")
        time.sleep(2)
