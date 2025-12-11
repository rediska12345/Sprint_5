import pytest
import sys
sys.path.append('..')
import locators

url = "https://stellarburgers.education-services.ru/"

@pytest.mark.parametrize("way", [
    "from_main",  # с главной
    "from_profile",  # из личного кабинета
])
def test_login_ways(driver, make_email, make_password, way):
    """Проверяем разные способы входа"""
    driver.get(url)
    
    if way == "from_main":
        driver.find_element(*locators.enter_button).click()
    else:
        driver.find_element(*locators.profile_link).click()
    
    # Вводим данные (сначала регистрируемся)
    email = make_email()
    password = make_password(6)
    
    # Регистрация для нового юзера
    driver.find_element(*locators.register_link).click()
    driver.find_element(*locators.name_input).send_keys("Тест")
    driver.find_element(*locators.email_input).send_keys(email)
    driver.find_element(*locators.pass_input).send_keys(password)
    driver.find_element(*locators.register_btn).click()
    
    # Возвращаемся на вход и входим
    driver.find_element(*locators.enter_button).click()
    driver.find_element(*locators.login_email).send_keys(email)
    driver.find_element(*locators.login_pass).send_keys(password)
    driver.find_element(*locators.login_btn).click()
    
    assert "account" in driver.current_url

