import locators
from conftest import driver

def test_constructor_tabs(driver):
    """Проверяю все вкладки конструктора"""
    driver.get("https://stellarburgers.education-services.ru/")
    
    # Кликаю Булки
    driver.find_element(*locators.TAB_BUNS).click()
    time.sleep(1)
    print("✅ Булки открылись!")
    
    # Кликаю Соусы
    driver.find_element(*locators.TAB_SAUCES).click()
    time.sleep(1)
    print("✅ Соусы открылись!")
    
    # Кликаю Начинки
    driver.find_element(*locators.TAB_FILLINGS).click()
    time.sleep(1)
    print("✅ Начинки открылись!")