import locators
from conftest import driver

email = "britvina_36@yandex.ru"
password = "12345678"

def login_to_profile(driver):
    #Вход и переход в профиль
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_PERSONAL_CABINET).click()
    driver.find_element(*locators.FIELD_EMAIL_LOGIN).send_keys(email)
    driver.find_element(*locators.FIELD_PASSWORD_LOGIN).send_keys(password)
    driver.find_element(*locators.BTN_LOGIN).click()
    driver.find_element(*locators.BTN_PERSONAL_CABINET).click()

def test_go_to_profile(driver):
    #Переход в личный кабинет
    login_to_profile(driver)
    profile_header = driver.find_element(*locators.HEADER_PROFILE)
    assert profile_header.is_displayed()

def test_logout(driver):
    #Выход из аккаунта
    login_to_profile(driver)
    driver.find_element(*locators.BTN_LOGOUT).click()
    assert "login" in driver.current_url

def test_profile_to_constructor(driver):
    #Из профиля в конструктор (кнопка)
    login_to_profile(driver)
    driver.find_element(*locators.BTN_CONSTRUCTOR).click()
    assert "constructor" in driver.current_url

def test_profile_to_logo(driver):
    #Из профиля в конструктор (логотип)
    login_to_profile(driver)
    driver.find_element(*locators.LOGO).click()
    assert "constructor" in driver.current_url