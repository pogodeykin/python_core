def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            return f"Лимит превышен: {actual_time} сек. > {max_time} сек."
        return f"Лимит не превышен: {actual_time} сек. <= {max_time} сек."

    return check_time


fast_test_checker = create_time_checker(2)
slow_test_checker = create_time_checker(5)

print(fast_test_checker(1.5))
print(fast_test_checker(3))

print(slow_test_checker(3))
print(slow_test_checker(6))
