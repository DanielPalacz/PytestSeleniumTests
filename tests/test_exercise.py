import pytest
from pytest_lazyfixture import lazy_fixture
from src.pom.columbus.registration import RegistryPage, ConfirmationPage


class TestRegistryFormSanity:
    @pytest.mark.parametrize("name, surname, phone, email",
                             [
                                 ("Jan", "Kowalski", "555393579", lazy_fixture("new_email"))
                             ],
                             )
    def test_user_registered(self, driver, name, surname, phone, email):
        registry_page = RegistryPage(driver)
        registry_page.fill_form(
            name=name,
            surname=surname,
            phone=phone,
            email=email,
        )
        assert registry_page.url == ConfirmationPage.URL
        confirmation_page = ConfirmationPage(driver)
        confirmation_msg = confirmation_page.get_confirmation_message()
        assert confirmation_msg == ConfirmationPage.MESSAGE

    @pytest.mark.parametrize("name", ["Jan", ""])
    @pytest.mark.parametrize("surname", ["Kowalski", ""])
    @pytest.mark.parametrize("phone", ["544582596", ""])
    @pytest.mark.parametrize("email", [lazy_fixture("new_email"), ""])
    def test_user_did_not_register_due_to_lack_of_data(self, driver, name, surname, phone, email):
        # additional skipping condition
        if all([name, surname, phone, email]):
            pytest.skip("test to be skipped because at least 1 input should be missing")

        registry_page = RegistryPage(driver)
        registry_page_url = registry_page.url
        registry_page.fill_form(
            name=name,
            surname=surname,
            phone=phone,
            email=email,
            expected_to_be_logged=False
        )
        assert registry_page_url == registry_page.url
        expected_validation_messages = self.__expected_validation_messages(
            name=name,
            surname=surname,
            phone=phone,
            email=email
        )
        assert expected_validation_messages == registry_page.get_input_validation_messages()

    @staticmethod
    def __expected_validation_messages(
            name: str,
            surname: str,
            phone: str,
            email: str
    ):
        validation_messages = dict()
        for k, v in locals().items():
            if k == "validation_messages":
                continue
            if not v:
                validation_messages.update({k: "Please fill out this field."})
            else:
                validation_messages.update({k: ""})
        return validation_messages
