import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from utils.wait_helper import WaitHelper

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BMIPage:

    URL = "https://diety.nfz.gov.pl"

    GENDER_SELECT = (
        By.ID,
        "plec"
    )

    AGE_INPUT = (
        By.ID,
        "wiek"
    )

    HEIGHT_INPUT = (
        By.ID,
        "wzrost"
    )

    WEIGHT_INPUT = (
        By.ID,
        "masa"
    )

    ACTIVITY_SELECT = (
        By.ID,
        "pal"
    )

    CALCULATE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Oblicz BMI')]"
    )

    BMI_RESULT = (
        By.XPATH,
        "//strong[contains(text(),'Waga')]"
    )

    COOKIE_BUTTON = (
        By.ID,
        "cookiehintsubmit"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)

    def open(self):

        self.driver.get(self.URL)

    def accept_cookies(self):

        try:

            button = self.wait.clickable(
                self.COOKIE_BUTTON,
                timeout=5
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        except:
            pass

    def select_gender(self, text):

        select = Select(
            self.wait.clickable(
                self.GENDER_SELECT
            )
        )

        select.select_by_visible_text(text)

    def enter_age(self, value):

        field = self.wait.visible(
            self.AGE_INPUT
        )

        field.clear()

        field.send_keys(value)

    def enter_height(self, value):

        field = self.wait.visible(
            self.HEIGHT_INPUT
        )

        field.clear()

        field.send_keys(value)

    def enter_weight(self, value):

        field = self.wait.visible(
            self.WEIGHT_INPUT
        )

        field.clear()

        field.send_keys(value)

    def select_activity(self, text):

        select = Select(
            self.wait.clickable(
                self.ACTIVITY_SELECT
            )
        )

        select.select_by_visible_text(text)

    def click_calculate(self):

        button = self.wait.clickable(
            self.CALCULATE_BUTTON
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def get_bmi_result(self):

        result = self.wait.visible(
            self.BMI_RESULT,
            timeout=20
        )

        return result.text.strip()

    def get_height_validation(self):

        field = self.driver.find_element(
            *self.HEIGHT_INPUT
        )

        return field.get_attribute(
            "validationMessage"
        )