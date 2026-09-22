users_password = "Python123"
for attempt in range(3):
    password = input("Введите пароль: ")
    if password == users_password:
        print("Добро пожаловать!")
        break
else:
    print("Доступ заблокирован")
