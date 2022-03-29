import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@pytest.fixture()
def driver():
    try:
        driver = webdriver.Chrome()
    except WebDriverException:
        raise
    driver.maximize_window()

    yield driver

    driver.quit()
