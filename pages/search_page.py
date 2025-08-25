import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.search_box = (By.ID, "q")

    def search_product(self, product_name):
        print(f"Searching for product: {product_name}")
        search_box = self.wait.until(EC.presence_of_element_located(self.search_box))
        search_box.send_keys(product_name)
        search_box.submit()

    def filter_by_brand(self, brand_name):
        business_value = brand_name.lower()
        
        # Wait for the element to be present first, then clickable
        checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//input[@businessvalue='{business_value}']")))
        
        # Then get the clickable label
        label = checkbox.find_element(By.XPATH, "./ancestor::label[1]")
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
        label.click()
        print(f"Clicked brand filter for: {brand_name}")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-qa-locator='product-item']")))
        # Optional: Add a small delay to ensure the DOM is fully updated
        time.sleep(1)

    def click_first_product(self):

        first_product = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-qa-locator='product-item'])[1]")))
    # Scroll to the product to ensure it's in view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_product)
        first_product.click()
        print("Clicked on the first product.")
        time.sleep(5)