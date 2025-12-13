import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit() #Настройка браузера
