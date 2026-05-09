import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():

    options = Options()

    options.binary_location = "/usr/bin/chromium-browser"

    options.add_argument("--start-maximized")

    options.add_argument("--incognito")

    options.add_argument("--no-sandbox")

    options.add_argument("--disable-dev-shm-usage")

    service = Service(
        "/usr/bin/chromedriver"
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs["driver"]

        driver.save_screenshot(
            f"reports/{item.name}.png"
        )