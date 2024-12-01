import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.skip
def test_example_with_implicit_wait(driver: WebDriver):
    driver.implicitly_wait(10)  # 10 second
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    heading = driver.find_element(By.TAG_NAME, "h7")
    assert heading.text == "Do more!"


@pytest.mark.skip
def test_example_with_explicit_wait(driver):
    driver.get("<https://www.example.com>")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    heading = driver.find_element_by_tag_name("h1")
    assert heading.text == "Example Domain"