from faker import Faker

from pages.registration_page import RegistrationPage


def test_registration_validation(driver):

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

    assert validation != ""