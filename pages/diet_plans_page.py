import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DietPlansPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    SELECT_PLAN_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Wybierz plan dla siebie')]"
    )

    CLASSIC_PLAN = (
        By.XPATH,
        "//*[contains(text(),'Classic')]"
    )

    KCAL_SELECT = (
        By.XPATH,
        "//select[@id='kalorycznosc_19']"
    )

    CHOOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'plan_19')]//input[@type='submit']"
    )

    STEP4_BUTTON = (
        By.XPATH,
        "//p[contains(@class,'mb-0')]//input[@type='submit']"
    )

    DAY_HEADER = (
        By.XPATH,
        "//div[contains(@class,'dieta_dzien')]//h2"
    )

    def click_choose_plan(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.SELECT_PLAN_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(5)

    def click_classic_plan(self):

        for _ in range(5):

            self.driver.execute_script(
                "window.scrollBy(0, 700);"
            )

            time.sleep(2)

        plans = self.driver.find_elements(
            *self.CLASSIC_PLAN
        )

        print("FOUND CLASSIC:", len(plans))

        for plan in plans:

            try:

                if plan.is_displayed():

                    print("CLICK CLASSIC")

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        plan
                    )

                    time.sleep(2)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        plan
                    )

                    time.sleep(3)

                    return

            except:
                pass

        raise Exception(
            "Classic plan not found"
        )

    def select_kcal(self):

        select = self.wait.until(
            EC.presence_of_element_located(
                self.KCAL_SELECT
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            select
        )

        time.sleep(2)

        self.driver.execute_script(
            "window.scrollBy(0, -300);"
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            select
        )

        time.sleep(2)

        option = self.driver.find_element(
            By.XPATH,
            "//select[@id='kalorycznosc_19']/option[3]"
        )

        self.driver.execute_script(
            "arguments[0].selected = true;",
            option
        )

        time.sleep(2)

    def click_choose(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CHOOSE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(3)

    def click_step4(self):

        buttons = self.driver.find_elements(
            *self.STEP4_BUTTON
        )

        for button in buttons:

            try:

                if button.is_displayed():

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        button
                    )

                    time.sleep(2)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        button
                    )

                    break

            except:
                pass

        time.sleep(3)

    def click_recipes(self):

        buttons = self.driver.find_elements(
            By.XPATH,
            "//input[@type='submit']"
        )

        for button in buttons:

            try:

                value = button.get_attribute("value")

                if value and "Przejdź do przepisów" in value:

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        button
                    )

                    time.sleep(2)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        button
                    )

                    break

            except:
                pass

        time.sleep(3)

    def is_day_visible(self):

        header = self.wait.until(
            EC.visibility_of_element_located(
                self.DAY_HEADER
            )
        )

        return header.is_displayed()