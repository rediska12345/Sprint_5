import locators
from conftest import driver

email = "britvina_36@yandex.ru"
password = "12345678"

def login(driver):
    #Просто вход
    driver.find_element(*locators.FIELD_EMAIL_LOGIN).send_keys(email)
    driver.find_element(*locators.FIELD_PASSWORD_LOGIN).send_keys(password)
    driver.find_element(*locators.BTN_LOGIN).click()
    time.sleep(2)

def test_login_main_button(driver):
    #Вход через кнопку на главной
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    login(driver)
    assert "constructor" in driver.current_url

def test_login_personal_cabinet(driver):
    #Вход через Личный кабинет
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_PERSONAL_CABINET).click()
    login(driver)

def test_login_from_register(driver):
    #Вход из формы регистрации
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    driver.find_element(*locators.LINK_REGISTER).click()
    driver.find_element(*locators.LINK_LOGIN_FROM_REGISTER).click()
    login(driver)

def test_login_from_recovery(driver):
    #Вход из формы восстановления пароля
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    driver.find_element(*locators.LINK_RECOVERY).click()
    driver.find_element(*locators.LINK_LOGIN_FROM_RECOVERY).click()
    login(driver)
