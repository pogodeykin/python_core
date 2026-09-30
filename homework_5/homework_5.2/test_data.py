import random


def generate_login():
    login = "user" + str(random.randint(0, 1000))
    return login


def generate_password():
    password = random.randint(18, 100)
    return password


def expected_result():
    return random.choice(['ACTIVE', 'BLOCKED', None])


def generate_user():
    return {
        'login': generate_login(),
        'password': generate_password(),
        'expected_result': expected_result()
    }
