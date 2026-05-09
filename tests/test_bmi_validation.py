import pytest

from faker import Faker

from pages.registration_page import RegistrationPage

from test_data.expected_messages import ExpectedMessages


@pytest.mark.registration
@pytest.mark.negative
def test_TC_03_registration_validation(driver):

    fake = Faker("pl_PL")

    page = RegistrationPage(driver)

    page.open()

    page.go_login()

    page.go_register()

    page.enter_register_email(
        fake.email()
    )

    page.enter_register_password("")

    validation = page.get_password_validation()

    assert validation != "", \
        ExpectedMessages.VALIDATION_MESSAGE