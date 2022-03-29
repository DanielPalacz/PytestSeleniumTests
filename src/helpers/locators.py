from typing import Tuple
from selenium.webdriver.common.by import By


class LocatorBuilder:

    @staticmethod
    def class_(value: str) -> Tuple[str, str]:
        return By.CLASS_NAME, value

    @staticmethod
    def id_(value: str) -> Tuple[str, str]:
        return By.ID, value

    @staticmethod
    def name(value: str) -> Tuple[str, str]:
        return By.NAME, value

    @staticmethod
    def xpath(value: str) -> Tuple[str, str]:
        return By.XPATH, value
