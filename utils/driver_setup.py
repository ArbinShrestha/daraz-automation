# utils/driver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # 🚀 Faster page loading (don’t wait for ads/images/scripts)
    options.page_load_strategy = "eager"

    # ✅ Cache driver so it doesn’t redownload every test run
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    return driver
