import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.login_button = (By.ID, "anonLogin") 
        self.email_input = (By.CSS_SELECTOR, "input[placeholder='Please enter your Phone or Email']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.submit_button = (By.XPATH, "//button[@type='button']")


    def go_to_home(self):
        print("Navigating to home page...")
        self.wait
        self.driver.get("https://www.daraz.com.np/")

    def login(self, email, password):
        print("Logging in...")
        login_btn = self.wait.until(EC.presence_of_element_located(self.login_button))
        login_btn.click()
         # Wait for login modal to appear and enter credentials
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        
        # Wait for login to complete - FIXED XPath
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='myAccountTrigger' and contains(text(), 'account')] | //a[@href='//member.daraz.com.np/user/logout']")))
            print("Login successful: User account element or logout link detected.")
        except Exception as e:
            print(f"Login may not have completed successfully: {e}")
            raise
        time.sleep(5)