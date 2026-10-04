import json
from main import main

main()  # позволил себе немножко фантазии,вызываю функцию по генерации файла с данными из прошлой домашки
# количество элементов фиксированно 6
# есть вопрос,как сделать чтобы в файле test_data.py в одном из элементов генерировалось отсутствующее значение?

file_name = "users.json"

try:
    with open(file_name, "r") as file:
        users = json.load(file)
        count = 0
    for user in users:
        try:
            count = count + 1
            print(f"Пользователь {count}: {user['login']}")
            print(f"Пароль: {user['password']}")
            print(f"Ожидаемый результат авторизации: {user['expected_result']}")
            print()
        except KeyError as e:
            missing_field = e.args[0]
            print(f'У пользователя {count} отсутствует обязательное поле"{missing_field}"')

except FileNotFoundError as e:
    print(f'Ошибка: не найден файл {file_name}')
except json.JSONDecodeError as e:
    print(f'содержимое файла {file_name} невозможно прочитать как JSON')
