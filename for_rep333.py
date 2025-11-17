def is_password_good(password):
    if len(password) < 8:
        return False
    a1 = False
    a2 = False
    a3 = False

    for a in password:
        if a.isupper():
            a1 = True
        elif a.islower():
            a2 = True
        elif a.isdigit():
            a3 = True
        return a1 and a2 and a3
from password_check import is_password_good

print("=== ПРОВЕРКА ПАРОЛЯ ===")

password = input("Введите пароль: ")
result = is_password_good(password)

if result:
    print("Пароль надежный")
else:
    print(" Пароль ненадежный")
    print("Требования:")
    print("- Не менее 8 символов")
    print("- Заглавные и строчные буквы") 
    print("- Цифры")
n = input()

print(is_password_good(n))
