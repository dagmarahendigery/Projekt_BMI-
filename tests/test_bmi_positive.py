import csv
import pytest

from pathlib import Path

from pages.bmi_page import BMIPage

from test_data.expected_messages import ExpectedMessages


DATA_FILE = Path(__file__).parent.parent / "data" / "bmi_data.csv"


def load_data():

    with open(DATA_FILE, encoding="utf-8") as file:

        return list(csv.DictReader(file))


@pytest.mark.bmi
@pytest.mark.positive
@pytest.mark.parametrize(
    "data",
    [load_data()[0]]
)
def test_TC_01_bmi_positive(driver, data):

    page = BMIPage(driver)

    page.open()

    page.accept_cookies()

    page.select_gender("Mężczyzna")

    page.enter_age("30")

    page.enter_height(data["height"])

    page.enter_weight(data["weight"])

    page.select_activity(data["activity"])

    page.click_calculate()

    result = page.get_bmi_result()

    assert data["expected_bmi"] in result, \
        ExpectedMessages.BMI_RESULT_FAILED