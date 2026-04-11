import pytest
import time
from selenium import webdriver
from pages.registration_page import RegistrationPage
from faker import Faker


@pytest.fixture
def driver():
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200, 1000)
    driver.set_window_position(0, 0)

    yield driver
    driver.quit()


def test_registration_flow(driver):
    page = RegistrationPage(driver)
    fake = Faker("pl_PL")

    email = fake.email()
    password = "Test1234!"

    # 1. wejście na stronę
    page.open()
    time.sleep(3)

    # 2. kliknij zaloguj
    page.go_login()
    time.sleep(3)

    # 3. kliknij zarejestruj się
    page.go_register()
    time.sleep(4)

    # 4. sprawdzenie URL
    print("CURRENT URL:", driver.current_url)
    time.sleep(3)

    # 5. uzupełnienie danych
    page.enter_email(email)
    time.sleep(2)

    page.enter_password(password)
    time.sleep(2)

    # 6. checkbox regulaminu
    page.accept_tos()
    time.sleep(2)

    # 7. pokaż hasło
    page.click_show_password()
    time.sleep(2)

    # 7. klik rejestruj
    page.submit()
    time.sleep(5)

    # asercja
    assert page.get_email() == email