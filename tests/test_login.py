import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import *
from helper import make_email, make_password

URL = "https://stellarburgers.education-services.ru/"
EMAIL = "britvina_36@yandex.ru"
PASS = "12345678"

def test_login_main_button(driver):
    #Вход по кнопке «Войти в аккаунт» на главной
    driver.get(URL)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

def test_login_personal_cabinet(driver):
    #Вход через кнопку «Личный кабинет»
    driver.get(URL)
    driver.find_element(MAIN_PERSONAL_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

def test_login_from_register(driver):
    #Вход через кнопку в форме регистрации
    driver.get(f"{URL}login")
    driver.find_element(REGISTER_LINK).click()
    driver.find_element(LOGIN_FROM_REG).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

def test_login_from_forgot_password(driver):
    #Вход через кнопку в форме восстановления пароля
    driver.get(f"{URL}login")
    driver.find_element(FORGOT_LINK).click()
    driver.find_element(LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

def test_profile_transitions_and_logout(driver):
    #Переход в ЛК"""
    driver.get(URL)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url
    
    # Переход на Конструктор
    driver.find_element(CABINET_CONSTRUCTOR).click()
    assert URL in driver.current_url
    
    # Переход по логотипу
    driver.find_element(LOGO).click()
    assert URL in driver.current_url
    
    # Выход (с главной заходим в ЛК и выходим)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    driver.find_element(LOGOUT_BUTTON).click()
    assert URL in driver.current_url

    