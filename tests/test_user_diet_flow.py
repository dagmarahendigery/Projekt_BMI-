import pytest

from pages.registration_page import RegistrationPage
from pages.diet_plans_page import DietPlansPage

from test_data.login_data import LoginData
from test_data.expected_messages import ExpectedMessages


@pytest.mark.diet
@pytest.mark.positive
def test_TC_05_logged_user_diet_flow(driver):

    registration = RegistrationPage(driver)

    registration.open()

    registration.go_login()

    registration.enter_login_email(
        LoginData.EMAIL
    )

    registration.enter_login_password(
        LoginData.PASSWORD
    )

    registration.click_show_password()

    registration.login_submit()

    assert registration.is_logged_in(), \
        ExpectedMessages.LOGIN_FAILED

    driver.get(
        "https://diety.nfz.gov.pl/plany-zywieniowe"
    )

    diet = DietPlansPage(driver)

    diet.click_choose_plan()

    diet.click_classic_plan()

    diet.select_kcal()

    diet.click_choose()

    diet.click_step4()

    diet.click_recipes()

    assert diet.is_day_visible(), \
        ExpectedMessages.DIET_DAY_FAILED