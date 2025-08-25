from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='Add to Cart']")
        add_to_cart_button.click()
