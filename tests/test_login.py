import pytest

from pages.registration_page import RegistrationPage

from test_data.login_data import LoginData
from test_data.expected_messages import ExpectedMessages


@pytest.mark.login
@pytest.mark.positive
def test_TC_04_login_success(driver):

    page = RegistrationPage(driver)

    page.open()

    page.go_login()

    page.enter_login_email(
        LoginData.EMAIL
    )

    page.enter_login_password(
        LoginData.PASSWORD
    )

    page.click_show_password()

    page.login_submit()

    assert page.is_logged_in(), \
        ExpectedMessages.LOGIN_FAILED