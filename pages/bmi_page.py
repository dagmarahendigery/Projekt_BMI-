from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BMIPage:
    URL = "https://diety.nfz.gov.pl/twoj-wskaznik-bmi"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # LOCATORS
    GENDER_SELECT = (By.ID, "plec")
    AGE_INPUT = (By.ID, "wiek")
    HEIGHT_INPUT = (By.ID, "wzrost")
    WEIGHT_INPUT = (By.ID, "masa")
    ACTIVITY_SELECT = (By.ID, "pal")

    CALCULATE_BUTTON = (By.XPATH, "//button[contains(text(),'Oblicz')]")
    RESULT = (By.XPATH, "//*[contains(text(),'BMI')]/following::*[contains(text(),'.')][1]")
    COOKIES = (By.ID, "cookiehintsubmit")

    # ACTIONS
    def open(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIES)).click()
        except TimeoutException:
            pass

    def set_zoom(self, value):
        self.driver.execute_script(f"document.body.style.zoom='{value}%'")

    def enter_age(self, value):
        el = self.wait.until(EC.element_to_be_clickable(self.AGE_INPUT))
        el.clear()
        el.send_keys(value)

    def enter_height(self, value):
        el = self.wait.until(EC.element_to_be_clickable(self.HEIGHT_INPUT))
        el.clear()
        el.send_keys(value)

    def get_height_value(self):
        return self.driver.find_element(*self.HEIGHT_INPUT).get_attribute("value")

    def enter_weight(self, value):
        el = self.wait.until(EC.element_to_be_clickable(self.WEIGHT_INPUT))
        el.clear()
        el.send_keys(value)

    def select_gender(self, text):
        el = self.wait.until(EC.element_to_be_clickable(self.GENDER_SELECT))
        Select(el).select_by_visible_text(text)

    def select_activity(self, text):
        el = self.wait.until(EC.element_to_be_clickable(self.ACTIVITY_SELECT))
        Select(el).select_by_visible_text(text)

    def click_calculate(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.CALCULATE_BUTTON))
        btn.click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_bmi(self):
        el = self.wait.until(EC.visibility_of_element_located(self.RESULT))
        text = el.text.strip()

        if not text:
            text = self.driver.find_element(By.XPATH, "//*[contains(text(),'BMI')]").text

        return text

    def get_kcal(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'kcal')]"))
        ).text

    def is_bmi_scale_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located((
                By.XPATH,
                "//*[contains(text(),'niedowaga') or contains(text(),'prawidłowa') or contains(text(),'nadwaga') or contains(text(),'otyłości')]"
            ))).is_displayed()
        except TimeoutException:
            return False

    def get_active_bmi_range(self):
        try:
            header = self.wait.until(EC.visibility_of_element_located((
                By.XPATH,
                "//*[contains(text(),'prawidłowa') or contains(text(),'nadwaga') or contains(text(),'otyłości')]"
            )))
            return header.text
        except TimeoutException:
            return None