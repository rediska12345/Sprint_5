from selenium.webdriver.common.by import By

# Главная страница
MAIN_PAGE_LOGO = (By.XPATH, "//div[@class='ReactModalPortal']//img[@alt='Stellar Burgers']")
LOGIN_BUTTON_HEADER = (By.XPATH, "//button[text()='Войти в аккаунт']")
PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[@href='/account']")

# Форма регистрации
REGISTER_TAB = (By.XPATH, "//a[text()='Зарегистрироваться']")
NAME_FIELD = (By.XPATH, "//input[@placeholder='Имя']")
EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Логин']")
PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Форма входа
LOGIN_EMAIL_FIELD = (By.ID, "email")  # или XPATH "//input[@placeholder='Email']"
LOGIN_PASSWORD_FIELD = (By.ID, "password")  # или XPATH "//input[@placeholder='Пароль']"
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Форма восстановления пароля
RECOVER_PASSWORD_TAB = (By.XPATH, "//a[text()='Восстановить пароль']")
RECOVER_EMAIL_FIELD = (By.ID, "email_recover")  # предположительный ID
RECOVER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # в форме восстановления

# Личный кабинет
PROFILE_CONSTRUCTOR_BUTTON = (By.XPATH, "//button[text()='Конструктор']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Конструктор
BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']")