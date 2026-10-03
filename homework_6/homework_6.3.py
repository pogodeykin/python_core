from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Тест завершён: {func.__name__}")
        print(f"Результат: {result}")

        return result

    return wrapper


@log_test
def test_login(username, password):
    return username == "admin" and password == "1234"


@log_test
def test_user_age(age, min_age=18):
    return age >= min_age


# Проверка функций
print(test_login("admin", "1234"))
print(test_user_age(21, min_age=18))
