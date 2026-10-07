from functools import wraps


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка №{attempt}")

                result = func(*args, **kwargs)

                if result is True:
                    print("Функция вернула True")
                    return True

            print("Все попытки завершились неудачно")
            return False

        return wrapper

    return decorator


attempts = 0


@retry(5)
def test_attempt():
    global attempts
    attempts += 1

    print("Попытка")

    return attempts >= 3


result = test_attempt()
print(f"Итоговый результат: {result}")
