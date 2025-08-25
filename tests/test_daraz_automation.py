import pytest
from utils.driver_setup import get_driver 
from pages.login_page import LoginPage
from pages.search_page import SearchPage



@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_daraz_flow(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.go_to_home()
    login_page.login()

    search_page = SearchPage(driver)
    search_page.search_product("laptop")
    search_page.filter_by_brand("Apple")
    search_page.click_first_product()

