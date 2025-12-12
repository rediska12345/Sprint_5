import locators
from conftest import driver

def test_constructor_tabs(driver):
    #Проверка вкладок конструктора
    driver.get("https://stellarburgers.education-services.ru/")
    
    # Клик Булки
    driver.find_element(*locators.TAB_BUNS).click()
    time.sleep(1)
    
    # Клик Соусы
    driver.find_element(*locators.TAB_SAUCES).click()
    time.sleep(1)
    
    # Клик Начинки
    driver.find_element(*locators.TAB_FILLINGS).click()
    time.sleep(1)
