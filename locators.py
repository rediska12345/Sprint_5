from selenium.webdriver.common.by import By

# Главная страница
BTN_ENTER_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
LOGO = (By.CLASS_NAME, "AppHeader_logo")  # логотип вверху

# Шапка сайта
BTN_PERSONAL_CABINET = (By.XPATH, "//p[text()='Личный Кабинет']")
BTN_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

# Форма входа
FIELD_EMAIL_LOGIN = (By.ID, "email")  # поле email для входа
FIELD_PASSWORD_LOGIN = (By.ID, "Пароль")  # поле пароль для входа
BTN_LOGIN = (By.XPATH, "//button[text()='Войти']")

# Форма регистрации  
FIELD_NAME = (By.ID, "Имя")  # поле Имя
FIELD_EMAIL_REGISTER = (By.ID, "email")  # поле Email регистрации
FIELD_PASSWORD_REGISTER = (By.ID, "Пароль")  # поле Пароль регистрации
BTN_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
ERROR_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

# Личный кабинет
BTN_LOGOUT = (By.XPATH, "//button[text()='Выход']")
HEADER_PROFILE = (By.XPATH, "//h2[text()='Профиль']")

# Конструктор бургера
TAB_BUNS = (By.XPATH, "//span[text()='Булки']")
TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']") 
TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")