import csv
import pytest
import time
from selenium import webdriver
from pages.bmi_page import BMIPage


def load_data():
    with open("data/bmi_data.csv") as f:
        return list(csv.DictReader(f))


@pytest.fixture(scope="module")
def driver():
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200, 1000)
    driver.set_window_position(0, 0)  #musi byc bo maximizie czasem crashuje
    yield driver #uruchamia test
    driver.quit() #zamyka test


def test_bmi_flow(driver):
    page = BMIPage(driver)
    data = load_data()

    #1. COOKIES
    page.open(); time.sleep(2)
    page.accept_cookies(); time.sleep(2)

    #2. SCENARIUSZ POZYTYWNY
    page.select_gender("Mężczyzna"); time.sleep(1)
    page.enter_age("30"); time.sleep(1)
    page.enter_height(data[0]["height"]); time.sleep(1)
    page.enter_weight(data[0]["weight"]); time.sleep(1)
    page.select_activity(data[0]["activity"]); time.sleep(1)

    page.click_calculate(); time.sleep(3)

    #SCROOLL DO WYKRESU BMI
    from selenium.webdriver.common.by import By

    bmi_chart = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div/div/div/div[4]/ul/li[1]/h3/strong")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", bmi_chart)
    time.sleep(3)

    #ODSWIEZENIE STRONY
    driver.refresh(); time.sleep(2)
    page.accept_cookies(); time.sleep(2)

    #2. SCENARIUSZ NEGATYWNY WALIDACJA PRZY BRAKU UZUPELNIONEGO POLA
    page.select_gender("Mężczyzna"); time.sleep(2)
    page.enter_age("30"); time.sleep(2)
    page.enter_height(""); time.sleep(2)  #pusty input ""
    page.enter_weight(data[-1]["weight"]); time.sleep(2)
    page.select_activity(data[-1]["activity"]); time.sleep(2)

    page.click_calculate(); time.sleep(2)

    height_input = driver.find_element(*page.HEIGHT_INPUT)

    #NIE SCROLLUJE DALEJ BO NIE MA WYNIKU
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", height_input)
    time.sleep(3)

    # sprawdzamy walidację HTML (formularz NIE powinien przejść dalej); strona wypuszcza kommunikat walidacyjny
    validation_message = height_input.get_attribute("validationMessage")
    print("DEBUG VALIDATION:", validation_message)

    time.sleep(3)  #WWERYFIKACJA KOMUNIKATU WALIDACYJNEGO

    assert validation_message != ""  #assert sprrawdza czy  walidacja zadzialala


    #4. MAKSYMALIZACJA / MINIMALIZACJA
    time.sleep(2)

    #DUŻE OKNO (symulacja maksymalizacji)
    driver.set_window_size(1600, 1000)
    print("WINDOW BIG")
    time.sleep(4)

    #MAŁE OKNO (symulacja minimalizacji)
    driver.set_window_size(800, 600)
    print("WINDOW SMALL")
    time.sleep(4)

    #RESET
    driver.set_window_size(1200, 1000)
    print("WINDOW RESET")
    time.sleep(3)