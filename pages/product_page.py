from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # Wait for the Add to Cart button to be clickable
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'add-to-cart-buy-now-btn') and .//span[text()='Add to Cart']]"))
        )
        # Scroll to the button to ensure it's in view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
        add_to_cart_button.click()
        print("Clicked 'Add to Cart' button.")
        # Optional: Wait for cart update confirmation (e.g., a cart popup or page change)
        time.sleep(2)
