def validate_age(age):
    if age < 0:
        raise ArithmeticError("Возраст не может быть отрицательным.")
    print(f"Возраст принят: {age}")


def get_user_age():
    try:
        age = int(input("Введите возраст: "))
        validate_age(age)
    except ArithmeticError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")


get_user_age()
