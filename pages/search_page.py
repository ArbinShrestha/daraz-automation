import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.search_box = (By.ID, "q")

    def search_product(self, product_name):
        search_box = self.wait.until(EC.presence_of_element_located(self.search_box))
        search_box.send_keys(product_name)
        search_box.submit()
        time.sleep(10)

    def filter_by_brand(self, brand_name):
        brand_filter = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//label[text()='{brand_name}']")))
        brand_filter.click()

    def click_first_product(self):
        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='product-item'])[1]")))
        first_product.click()
