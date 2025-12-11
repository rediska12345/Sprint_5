import time
import locators
from conftest import driver

email = "britvina_36@yandex.ru"
password = "12345678"

def test_good_register(driver):
    """Проверяю успешную регистрацию с правильными данными"""
    driver.get("https://stellarburgers.education-services.ru/")
    
    # Кликаю "Войти в аккаунт"
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    
    # Кликаю "Зарегистрироваться" 
    driver.find_element(*locators.LINK_REGISTER).click()
    
    # Заполняю форму
    driver.find_element(*locators.FIELD_NAME).send_keys("Тест")
    driver.find_element(*locators.FIELD_EMAIL_REGISTER).send_keys(email)
    driver.find_element(*locators.FIELD_PASSWORD_REGISTER).send_keys(password)
    
    # Отправляю форму
    driver.find_element(*locators.BTN_REGISTER).click()
    
    # Проверяю, что попал на страницу входа (успешная регистрация)
    time.sleep(2)
    assert "login" in driver.current_url
    print("✅ Регистрация прошла успешно!")

def test_bad_password(driver):
    """Проверяю ошибку при коротком пароле"""
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*locators.BTN_ENTER_MAIN).click()
    driver.find_element(*locators.LINK_REGISTER).click()
    
    # Заполняю с коротким паролем (5 символов)
    driver.find_element(*locators.FIELD_NAME).send_keys("Тест")
    driver.find_element(*locators.FIELD_EMAIL_REGISTER).send_keys("test@test.ru")
    driver.find_element(*locators.FIELD_PASSWORD_REGISTER).send_keys("12345")
    driver.find_element(*locators.BTN_REGISTER).click()
    
    # Проверяю ошибку
    error = driver.find_element(*locators.ERROR_PASSWORD)
    assert error.is_displayed()
    print("✅ Ошибка пароля работает!")