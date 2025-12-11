import pytest
from selenium.webdriver.common.by import By
import locators

BASE_URL = "https://stellarburgers.education-services.ru/"

def test_successful_registration(driver, generate_email, generate_password, wait):
    """Успешная регистрация с корректными данными"""
    driver.get(BASE_URL)
    
    # Клик на регистрацию
    wait.until(EC.element_to_be_clickable(locators.REGISTER_TAB)).click()
    
    # Заполнение формы
    email = generate_email()
    password = generate_password(8)
    
    wait.until(EC.visibility_of_element_located(locators.NAME_FIELD)).send_keys("Тест")
    driver.find_element(*locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*locators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()
    
    # Проверка перехода в личный кабинет
    assert "account" in driver.current_url, "Регистрация не привела в личный кабинет"

def test_registration_invalid_password(driver, generate_email, generate_password, wait):
    """Ошибка при регистрации с коротким паролем"""
    driver.get(BASE_URL)
    
    wait.until(EC.element_to_be_clickable(locators.REGISTER_TAB)).click()
    
    email = generate_email()
    short_password = generate_password(3)  # Слишком короткий
    
    driver.find_element(*locators.NAME_FIELD).send_keys("Тест")
    driver.find_element(*locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*locators.PASSWORD_FIELD).send_keys(short_password)
    driver.find_element(*locators.REGISTER_BUTTON).click()
    
    # Проверка ошибки (предполагаем, что появляется красная подсветка или сообщение)
    password_field = driver.find_element(*locators.PASSWORD_FIELD)
    assert "error" in password_field.get_attribute("class").lower(), "Ошибка не отобразилась"