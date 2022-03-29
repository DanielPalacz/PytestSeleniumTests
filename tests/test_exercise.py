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
    def test_did_not_user_register_lack_of_data(self, driver, name, surname, phone, email):
        pass
