from faker import Faker
faker = Faker()

def generate_email():
    username = faker.username()
    domain = 'ya.ru'
    return f"{username}@{domain}"

def generate_valid_password():
    password = faker.password(length=8, special_chars=True, digits=True,upper_case=True,lower_case=True)
    return password

def generate_invalid_password():
    password = faker.password(length=4, special_chars=True, digits=True,upper_case=True,lower_case=True)
    return password #Генерируется пароль короче 6 символов