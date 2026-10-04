import json
from test_data import generate_user


def main():
    data = []
    for _ in range(6):
        data.append(generate_user())
    with open("users.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
