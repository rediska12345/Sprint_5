import time
import locators
from conftest import driver

email = "britvina_36@yandex.ru"
password = "12345678"

def test_good_register(driver):
    #Проверка успешной регистрации с валидными данными
    driver.get("https://stellarburgers.education-services.ru/")
    
    # Клик "Войти в аккаунт"
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    
    # Клик "Зарегистрироваться" 
    driver.find_element(*locators.LINK_REGISTER).click()
    
    # Заполнение формы
    driver.find_element(*locators.FIELD_NAME).send_keys("Тест")
    driver.find_element(*locators.FIELD_EMAIL_REGISTER).send_keys(email)
    driver.find_element(*locators.FIELD_PASSWORD_REGISTER).send_keys(password)
    
    # Отправка формы
    driver.find_element(*locators.BTN_REGISTER).click()
    
    # Проверка, что попал на страницу входа (успешная регистрация)
    time.sleep(2)
    assert "login" in driver.current_url

def test_bad_password(driver):
    #Проверка ошибки при коротком пароле
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    driver.find_element(*locators.LINK_REGISTER).click()
    
    # Короткий пароль(5 символов)
    driver.find_element(*locators.FIELD_NAME).send_keys("Тест")
    driver.find_element(*locators.FIELD_EMAIL_REGISTER).send_keys("test@test.ru")
    driver.find_element(*locators.FIELD_PASSWORD_REGISTER).send_keys("12345")
    driver.find_element(*locators.BTN_REGISTER).click()
    
    # Проверка ошибки
    error = driver.find_element(*locators.ERROR_PASSWORD)
    assert error.is_displayed()
    