from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_count(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "cart-num")
        return int(cart_icon.text)
