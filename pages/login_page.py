from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.login_button = (By.ID, "anonLogin") 


    def go_to_home(self):
        print("Navigating to home page...")
        self.wait
        self.driver.get("https://www.daraz.com.np/")

    def login(self):
        print("Logging in...")
        login_btn = self.wait.until(EC.presence_of_element_located(self.login_button))
        login_btn.click()     
       