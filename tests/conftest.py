from datetime import datetime

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


@pytest.fixture()
def new_email(get_timestamp):
    numerical_timestamp = int(get_timestamp)
    return f"test+{hex(numerical_timestamp)}@gmail.com"


@pytest.fixture()
def get_timestamp() -> str:
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H%M%S")
    return year + month + day + time
