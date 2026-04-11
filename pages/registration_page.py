from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    LOGIN = (By.XPATH, "/html/body/header/div[3]/div/div/div/a")
    REGISTER = (By.XPATH, "/html/body/div[4]/div[2]/form/fieldset/div[4]/a[1]")

    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//*[@id='jform_password1']")
    TOS = (By.XPATH, "//*[@id='jform_profile_tos0']")
    SHOW_PASSWORD = (By.XPATH, "/html/body/main/div/div/form/fieldset[1]/div[2]/div[2]/div[2]/div/button")
    SUBMIT = (By.XPATH, "/html/body/main/div/div/form/div[2]/div/button")

    def open(self):
        self.driver.get("https://diety.nfz.gov.pl/twoj-wskaznik-bmi") #otwietastroneglowna

    def go_login(self):
        try:
            self.driver.find_element(By.ID, "cookiehintsubmit").click()
        except:
            pass

        el = self.wait.until(EC.presence_of_element_located(self.LOGIN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN)).click()

    def go_register(self):
        el = self.wait.until(EC.presence_of_element_located(self.REGISTER))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        self.wait.until(EC.element_to_be_clickable(self.REGISTER)).click()

    def enter_email(self, value):
        el = self.wait.until(EC.element_to_be_clickable(self.EMAIL))
        el.clear()
        el.send_keys(value)

    def enter_password(self, value):
        el = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        el.clear()
        el.send_keys(value)

    def accept_tos(self):
        el = self.wait.until(EC.element_to_be_clickable(self.TOS))
        el.click()

    def click_show_password(self):
        el = self.wait.until(EC.element_to_be_clickable(self.SHOW_PASSWORD))
        el.click()

    def submit(self):
        el = self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        el.click()

    def get_email(self):
        return self.driver.find_element(*self.EMAIL).get_attribute("value")

    def get_password(self):
        return self.driver.find_element(*self.PASSWORD).get_attribute("value")