import pytest
from selenium.webdriver.common.by import By
import locators

BASE_URL = "https://stellarburgers.education-services.ru/"
TEST_EMAIL = "test@stellarburgers.test"
TEST_PASSWORD = "123456"

@pytest.mark.parametrize("login_method", [
    "header_button",
    "personal_cabinet", 
    "register_form",
    "recover_form"
])
def test_login_methods(driver, generate_email, generate_password, wait, login_method):
    """Проверка всех способов входа"""
    driver.get(BASE_URL)
    
    if login_method == "header_button":
        wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_HEADER)).click()
    elif login_method == "personal_cabinet":
        wait.until(EC.element_to_be_clickable(locators.PERSONAL_CABINET_BUTTON)).click()
    elif login_method == "register_form":
        wait.until(EC.element_to_be_clickable(locators.REGISTER_TAB)).click()
        login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']")))
        login_link.click()
    elif login_method == "recover_form":
        wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_HEADER)).click()
        wait.until(EC.element_to_be_clickable(locators.RECOVER_PASSWORD_TAB)).click()
        login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
        login_link.click()
    
    # Вход в аккаунт
    email = generate_email()
    password = generate_password(8)
    
    wait.until(EC.visibility_of_element_located(locators.LOGIN_EMAIL_FIELD)).send_keys(email)
    driver.find_element(*locators.LOGIN_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    
    assert "account" in driver.current_url, f"Не удалось войти через {login_method}"