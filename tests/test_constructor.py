import pytest
from selenium.webdriver.common.by import By
import locators

BASE_URL = "https://stellarburgers.education-services.ru/"

def test_profile_to_constructor_navigation(driver, generate_email, generate_password, wait):
    """Переходы между личным кабинетом и конструктором"""
    driver.get(BASE_URL)
    
    # Вход
    wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_HEADER)).click()
    email = generate_email()
    password = generate_password(8)
    
    driver.find_element(*locators.LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*locators.LOGIN_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    
    # Переход в конструктор из профиля
    wait.until(EC.element_to_be_clickable(locators.PROFILE_CONSTRUCTOR_BUTTON)).click()
    assert "/#" in driver.current_url, "Не перешли в конструктор из профиля"
    
    # Обратно в конструктор через логотип
    driver.find_element(*locators.MAIN_PAGE_LOGO).click()
    assert "react=menu" not in driver.current_url, "Логотип не работает"

def test_profile_logout(driver, generate_email, generate_password, wait):
    """Выход из аккаунта"""
    driver.get(BASE_URL)
    
    # Вход
    wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_HEADER)).click()
    email = generate_email()
    password = generate_password(8)
    
    driver.find_element(*locators.LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*locators.LOGIN_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    
    # Выход
    wait.until(EC.element_to_be_clickable(locators.LOGOUT_BUTTON)).click()
    assert driver.current_url == BASE_URL, "Выход не сработал"

def test_constructor_tabs(driver, generate_email, generate_password, wait):
    """Работа вкладок конструктора"""
    driver.get(BASE_URL)
    
    # Вход и переход в конструктор
    wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_HEADER)).click()
    email = generate_email()
    password = generate_password(8)
    
    driver.find_element(*locators.LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*locators.LOGIN_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    
    wait.until(EC.element_to_be_clickable(locators.PROFILE_CONSTRUCTOR_BUTTON)).click()
    
    # Проверка вкладок
    tabs = [
        locators.BUNS_TAB,
        locators.SAUCES_TAB,
        locators.TOPPINGS_TAB
    ]
    
    for tab_locator in tabs:
        tab = wait.until(EC.element_to_be_clickable(tab_locator))
        tab.click()
        assert tab.get_attribute("class").find("active") != -1, "Вкладка не активировалась"