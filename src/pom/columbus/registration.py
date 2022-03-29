from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.helpers.locators import LocatorBuilder
from src.pom.common import BasePage


class RegistryPageLocators:
    NAME = LocatorBuilder.id_(value="name")
    SURNAME = LocatorBuilder.id_(value="lastName")
    PHONE = LocatorBuilder.id_(value="phone")
    EMAIL = LocatorBuilder.id_(value="email")
    REGISTRATION_BUTTON = \
        LocatorBuilder.xpath(value="//form[@id='signUpForm']/button")


class RegistryPage(BasePage):
    URL = "http://care.pureinteractive.pl/?mod=signUp"

    def __init__(
            self,
            driver: WebDriver
    ) -> None:
        super().__init__(driver)
        self.open(self.URL)

    def fill_form(
            self,
            name: str,
            surname: str,
            phone: str,
            email: str
    ) -> None:
        self.type(RegistryPageLocators.NAME, name)
        self.type(RegistryPageLocators.SURNAME, surname)
        self.type(RegistryPageLocators.PHONE, phone)
        self.type(RegistryPageLocators.EMAIL, email)
        self.click(RegistryPageLocators.REGISTRATION_BUTTON)
        self.wait.until(
            expected_conditions.url_to_be(ConfirmationPage.URL)
        )


class RegistryConfirmationPageLocators:
    CONFIRMATION_MESSAGE = \
        LocatorBuilder.xpath(
            value="//h4[contains(text(),"
                  "'Na Twój adres email wysłaliśmy link do aktywacji konta')]"
        )


# Na Twój adres email wysłaliśmy link do aktywacji konta


class ConfirmationPage(BasePage):
    MESSAGE = "Na Twój adres email wysłaliśmy link do aktywacji konta"
    URL = "http://care.pureinteractive.pl/?mod=signUp&msg=s_registerLead"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_confirmation_message(self) -> str:
        self.wait.until_not(
            expected_conditions.staleness_of(
                self.find_element(
                    RegistryConfirmationPageLocators.CONFIRMATION_MESSAGE
                )))
        return self.find_element(
            RegistryConfirmationPageLocators.CONFIRMATION_MESSAGE
        ).text
