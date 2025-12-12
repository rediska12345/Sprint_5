import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import *

URL = "https://stellarburgers.education-services.ru/"
EMAIL = "britvina_36@yandex.ru"
PASS = "12345678"

def login_and_go_constructor(driver):
    #Вход и переход в конструктор
    driver.get(URL)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(PASS)
    driver.find_element(LOGIN_BUTTON).click()
    driver.find_element(CABINET_CONSTRUCTOR).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUNS_TAB))

def test_buns_tab(driver):
    #Переход к разделу «Булки»
    login_and_go_constructor(driver)
    driver.find_element(BUNS_TAB).click()
    assert driver.find_element(BUNS_TAB).is_displayed()

def test_sauces_tab(driver):
    #Переход к разделу «Соусы»
    login_and_go_constructor(driver)
    driver.find_element(SAUCES_TAB).click()
    assert driver.find_element(SAUCES_TAB).is_displayed()

def test_fillings_tab(driver):
    #Переход к разделу «Начинки»
    login_and_go_constructor(driver)
    driver.find_element(FILLINGS_TAB).click()
    assert driver.find_element(FILLINGS_TAB).is_displayed()