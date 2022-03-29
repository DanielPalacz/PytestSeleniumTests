from typing import Dict

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

from src.helpers.locators import LocatorBuilder
from src.pom.common import BasePage


class RegistryPageLocators:
    NAME = LocatorBuilder.id_(value="name")
    SURNAME = LocatorBuilder.id_(value="lastName")
    PHONE = LocatorBuilder.id_(value="phone")
    EMAIL = LocatorBuilder.id_(value="email")
    REGISTRATION_BUTTON = \
        LocatorBuilder.xpath(value="//form[@id='signUpForm']/button")

    @classmethod
    def get_form_input_locators(cls) -> Dict:
        return {
            "name": cls.NAME,
            "surname": cls.SURNAME,
            "phone": cls.PHONE,
            "email": cls.EMAIL
        }


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
            email: str,
            expected_to_be_logged: bool = True
    ) -> None:
        self.type(RegistryPageLocators.NAME, name)
        self.type(RegistryPageLocators.SURNAME, surname)
        self.type(RegistryPageLocators.PHONE, phone)
        self.type(RegistryPageLocators.EMAIL, email)
        self.click(RegistryPageLocators.REGISTRATION_BUTTON)
        if expected_to_be_logged:
            self.wait.until(
                expected_conditions.url_to_be(ConfirmationPage.URL)
            )

    def get_input_validation_messages(self) -> Dict:
        """
        example of returned validation Dict:
        {'name': 'Please fill out this field.', 'surname': '', 'phone': '', 'email': ''}
        """
        validation_messages = dict()
        for k, v in RegistryPageLocators.get_form_input_locators().items():
            validation_messages.update({k: self.get_validation_message_attribute(v)})
        return validation_messages


class RegistryConfirmationPageLocators:
    CONFIRMATION_MESSAGE = \
        LocatorBuilder.xpath(
            value="//h4[contains(text(),"
                  "'Na Twój adres email wysłaliśmy link do aktywacji konta')]"
        )


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
