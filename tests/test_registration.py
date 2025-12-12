import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import *
from helper import make_email, make_password, make_user

URL = "https://stellarburgers.education-services.ru/"

def test_good_registration(driver):
    driver.get(f"{URL}login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_LINK)).click()
    user = make_user()
    driver.find_element(REG_NAME).send_keys(user['name'])
    driver.find_element(REG_EMAIL).send_keys(user['email'])
    driver.find_element(REG_PASSWORD).send_keys(user['password'])
    driver.find_element(REG_BUTTON).click()
    assert "/account" in driver.current_url #Проверка успешной регистрации

def test_bad_password(driver: WebDriver):
    driver.get(f"{URL}login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_LINK)).click()
    driver.find_element(REG_NAME).send_keys("Тест")
    driver.find_element(REG_EMAIL).send_keys(make_email())
    driver.find_element(REG_PASSWORD).send_keys("123")
    driver.find_element(REG_BUTTON).click()
    error = WebDriverWait(driver, 5).until(EC.presence_of_element_located(PASSWORD_ERROR))
    assert "Некорректный пароль" in error.text #Проверка ошибки при пароле менее 6 знаков
