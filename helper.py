import random
import string

def make_email():
    number = random.randint(1000, 9999)
    return f"test{number}@yandex.ru" #Эмейл

def make_password(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length)) #Пароль из цифр и букв

def make_user():
    return {
        'name': 'Тест',
        'email': make_email(),
        'password': make_password()
    } #Полные регистрационные данные

