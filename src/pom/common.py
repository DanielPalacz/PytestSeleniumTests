from typing import Tuple, List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, 0.5)

    @property
    def url(self):
        return self.driver.current_url

    def click(self, locator: Tuple[str, str]) -> None:
        self.driver.find_element(*locator).click()

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    def get_attribute(self, locator: Tuple[str, str], attribute: str) -> str:
        return self.driver.find_element(*locator).get_attribute(attribute)

    def get_validation_message_attribute(self, locator: Tuple[str, str]) -> str:
        return self.driver.find_element(*locator).get_attribute("validationMessage")

    def open(self, url: str) -> None:
        self.driver.get(url)

    def type(self, locator: Tuple[str, str], text: str) -> None:
        self.driver.find_element(*locator).send_keys(text)
