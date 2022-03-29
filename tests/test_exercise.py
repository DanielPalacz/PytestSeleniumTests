from src.pom.columbus.registration import RegistryPage, ConfirmationPage


class TestRegistryForm:

    # def test_user_registered(self, driver, name, surname, phone, email):
    def test_user_registered(self, driver):
        registry_page = RegistryPage(driver)
        registry_page.fill_form(
            name="x1",
            surname="x1",
            phone="555393579",
            email="x9@com",
        )
        assert registry_page.url == ConfirmationPage.URL
        confirmation_page = ConfirmationPage(driver)
        confirmation_msg = confirmation_page.get_confirmation_message()
        assert confirmation_msg == ConfirmationPage.MESSAGE

    def test_did_not_user_register_lack_of_data(self, driver):
        pass
