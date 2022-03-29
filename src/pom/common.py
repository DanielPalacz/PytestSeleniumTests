from typing import Tuple, List

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: Tuple[str, str]) -> None:
        self.driver.find_element(*locator).click()

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def type(self, locator: Tuple[str, str], text: str) -> None:
        self.driver.find_element(*locator).send_keys(text)
