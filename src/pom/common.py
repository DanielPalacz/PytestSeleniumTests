from typing import Tuple, List

from selenium import webdriver


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def click(self, locator: Tuple[str, str]) -> None:
        self.driver.find_element(*locator).click()

    def find_element(self, locator: Tuple[str, str]) -> webdriver:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Tuple[str, str]) -> List[webdriver]:
        return self.driver.find_elements(*locator)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def type(self, locator: Tuple[str, str], text: str) -> None:
        self.driver.find_element(*locator).send_keys(text)
