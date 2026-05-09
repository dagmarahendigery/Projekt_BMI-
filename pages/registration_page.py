from selenium.webdriver.common.by import By

from utils.wait_helper import WaitHelper


class RegistrationPage:

    URL = "https://diety.nfz.gov.pl"

    LOGIN_BUTTON = (
        By.XPATH,
        "//a[contains(.,'Zaloguj')]"
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'register')]"
    )

    LOGIN_EMAIL = (
        By.NAME,
        "username"
    )

    LOGIN_PASSWORD = (
        By.NAME,
        "password"
    )

    LOGIN_SUBMIT = (
        By.XPATH,
        "//button[contains(text(),'Zaloguj')]"
    )

    REGISTER_EMAIL = (
        By.ID,
        "jform_email1"
    )

    REGISTER_PASSWORD = (
        By.ID,
        "jform_password1"
    )

    SHOW_PASSWORD = (
        By.XPATH,
        "//span[contains(@class,'input-password-show')]"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Wyloguj')]"
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

            button = self.wait.presence(
                self.COOKIE_BUTTON,
                timeout=10
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        except:
            pass

    def go_login(self):

        self.accept_cookies()

        button = self.wait.presence(
            self.LOGIN_BUTTON,
            timeout=20
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def go_register(self):

        button = self.wait.presence(
            self.REGISTER_BUTTON,
            timeout=20
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.presence(
            self.REGISTER_EMAIL
        )

    def enter_login_email(self, email):

        field = self.wait.visible(
            self.LOGIN_EMAIL
        )

        field.clear()

        field.send_keys(email)

    def enter_login_password(self, password):

        field = self.wait.visible(
            self.LOGIN_PASSWORD
        )

        field.clear()

        field.send_keys(password)

    def click_show_password(self):

        try:

            button = self.wait.presence(
                self.SHOW_PASSWORD
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        except:
            pass

    def login_submit(self):

        button = self.wait.presence(
            self.LOGIN_SUBMIT,
            timeout=20
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def enter_register_email(self, email):

        field = self.wait.visible(
            self.REGISTER_EMAIL
        )

        field.clear()

        field.send_keys(email)

    def enter_register_password(self, password):

        field = self.wait.visible(
            self.REGISTER_PASSWORD
        )

        field.clear()

        field.send_keys(password)

    def logout(self):

        button = self.wait.presence(
            self.LOGOUT_BUTTON,
            timeout=20
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def get_password_validation(self):

        field = self.driver.find_element(
            *self.REGISTER_PASSWORD
        )

        return field.get_attribute(
            "validationMessage"
        )
    def is_logged_in(self):

        return "wyloguj" in self.driver.page_source.lower()

    def is_logged_out(self):

        return "zaloguj" in self.driver.page_source.lower()