# 1. Создайте функцию make_coffee(name, sugar, milk), которая выводит, что за кофе будет приготовлен. Причем сахар и молоко можно и не добавлять.
# Пример:

# make_coffee("Latte") ➝ Latte with 1 sugar and no milk
# make_coffee("Espresso", 0, True) ➝ Espresso with 0 sugar and with milk

# def make_coffee(name, sugar=0, milk=False):
#     print("Order 🔔:")

#     if (milk == True):
#         print(f"User ordered ☕ {name} with {sugar} tsp of sugar and milk")
#     else:
#         print(f"User ordered ☕ {name} with {sugar} tsp of sugar and no milk")


# make_coffee("Latte", sugar=2, milk=True)
# make_coffee("Espresso")


# def make_coffee(name, sugar=0, milk=False):
#     print("Order 🔔:")
#     isMilkOrdered = 'and no milk'

#     if (milk == True):
#         isMilkOrdered = "and with milk"

#     print(f"User ordered ☕ {name} with {sugar} tsp of sugar {isMilkOrdered}")


# make_coffee("Latte", sugar=2, milk=True)
# print()
# make_coffee("Espresso")


# 2. Напишите функцию longest_word(*words), которая принимает любое количество слов и возвращает самое длинное.
# Пример:

# longest_word("apple", "banana", "strawberry") ➝ "strawberry"


# def longest_word(*args):
#     theLongestWord = args[0]
#     index = 1

#     while (index < len(args)):

#         if (len(args[index]) > len(theLongestWord)):
#             theLongestWord = args[index]

#         index += 1

#     return theLongestWord

# def longest_word(*args):
#     theLongestWord = args[0]
#     for element in args:
#         if (len(element) > len(theLongestWord)):
#             theLongestWord = element

#     return theLongestWord


# names = ["Ali", "Farhad", "Esmiralda", "Samir"]
# result = longest_word(*names)
# print(result)


# 3.  Напишите функцию generate_password(length, include_special), которая возвращает случайный пароль из латинских букв. include_special - опциональный параметр. Если include_special=True, добавьте спецсимволы. Используйте модули random и string.

# import random
# import string


# def generatePassword(length, include_special=False):
#     charactersPool = string.ascii_letters

#     if include_special == True:
#         charactersPool += string.punctuation

#     passwordList = random.choices(charactersPool, k=length)
#     password = ''.join(passwordList)
#     print(password)


# generatePassword(18, True)

# 4. Вложенные функции для расчёта налога
# Нужно создать калькулятор запрлаты.
# Функция calculate_salary(base, bonus) должна использовать внутреннюю функцию apply_tax(salary) — она уменьшает зарплату на 14% налога. Верните итоговую сумму после налога и бонуса. Также для ф-ции calculate_salary создайте подсказки.

# def calculate_salary(base: float, bonus: float) -> float:
#     print("Your GROS salary:", base)

#     def apply_tax(salary: float) -> float:
#         return salary * 0.86
#     base = apply_tax(base)
#     total = base + bonus
#     print("Your NET salary: ", base)
#     print("Your salary with bonus", total )
#     return total

# result = calculate_salary(1000,200)
# print(result)

# 5. Расширяемое меню
# Создайте функцию menu(title, options) — печатает заголовок и нумерованные пункты меню, где options - пара­метры, переданные через запятую в ф-цию.
# Пример:
# а) menu("Main Menu", "Start", "Settings", "Exit")

# Main Menu:
# 1. Start
# 2. Settings
# 3. Exit

# b) menu("Step It Catering", "Book a place", "Reservations", "Food of the day", "Price list", "Exit")
# Step It Catering
# 1. Book a place
# 2. Reservations
# 3. Food of the day
# 4. Price list
# 5. Exit

# def menu(title, *args):
#     print(title)
#     order = 1
#     for option in args:
#         print(f"{order}. {option}")
#         order += 1


# options = ["Book a place", "Reservations",
#     "Food of the day", "Price list", "Exit"]

# title = "Step it food"
# menu(title, *options)

# 6. Вызов функции внутри функции
# Описание:
# Напишите функцию validate_and_square(n):

# Внутри неё функция is_number(n), которая проверяет, что n — целое положитльное число.

# Если число — вернуть n**2, иначе — None.

# def is_number(userInput: str) -> bool:
#     return str.isdigit(userInput)


# def validate_and_square(userInput: str) -> float:
#     if (is_number(userInput)):
#         return float(userInput) ** 2
#     return None


# print(validate_and_square("hello"))

# 7. Список функций
# Описание:
# Создайте список из трёх функций (add, sub, mul). Напишите функцию apply_all(funcs, a, b) — она применяет все функции к a и b и возвращает список результатов.

# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# def mul(a, b):
#     return a * b


# def apply_all(*args, a, b):
#     results = []
#     for action in functions:
#         results.append(action(a, b))
#     return results


# functions = [add, sub, mul]
# result = apply_all(*functions, 10, 5)
# print(result)


# 8. Вызов ф-ции внутри другой ф-ции (не вложенные 😄)
# Описание:
# Создайте функцию is_palindrome(s: str) -> bool. Затем создайте функцию check_all(*words) — она использует is_palindrome() и возвращает список только палиндромов из всех слов.

# def is_palindrome(s: str) -> bool:
#     reversedWord = s[::-1]
#     if (s == reversedWord):
#         return True
#     else:
#         return False


# def check_all(*args):
#     only_palindromes = []
#     for word in args:
#         if (is_palindrome(word) == True):
#             only_palindromes.append(word)

#     return only_palindromes


# words = ["alla", "искатьтакси", "kamran", "bob", "123321", "hello"]
# result = check_all(*words)
# print(result)

# 9. Именованные параметры + типизация
# Описание:
# Напишите функцию def circleArea, которая принимает только именованные параметры и возвращает площадь круга. Используйте hinting (подсказки при наведении)

# def areaCircle(radius: float) -> float:
#     pi = 3.14
#     return pi * (radius ** 2)


# print(areaCircle(radius=1))

# 10. Углублённая работа с args и фильтрацией
# Описание:
# Функция unique_sorted_numbers(*args) должна:

# def unique_sorted_numbers(*args):
#     uniqueNumbers = set(args)
#     uniqueEvenNumbers = []
#     for number in uniqueNumbers:
#         if (number % 2 == 0):
#             uniqueEvenNumbers.append(number)
#     print(uniqueEvenNumbers)


# unique_sorted_numbers(1, 1, 3, 4, 5, 62, 4, 5, 1)

# 👉 Принять любое количество чисел;

# 👉 Удалить повторы;

# 👉 Отфильтровать нечётные;

# 👉 Вернуть отсортированный список чётных чисел.

# 11.
# Описание:

# Функция build_route(start, *points, end = "Home")

# Возвращает строку маршрута:

# (Попытайтесь по сигнатуре ф-ции понять какие параметры она принимает, что из них обязательно, какие упакованы и т.п.)
# Так если я хочу выйти из Баку и через несколько городов вернуться домой, то:
# Route: Baku → Ganja → Sheki → Home

def build_route(*points, start, end="Home"):
    print(start, end=" → ")
    for point in points:
        print(point, end=' → ')
    print(end)


points = ["Sheki", "Ganja", "Lenkaran", "Astara", "Lerik"]
build_route("Sheki", "Ganja", start="Baku", end="Baku")


# 12 Перевести десятичное число в 2чное

# def decimal_to_binary(n):
#     if n == 0:
#         return "0"

#     bits = []
#     while n > 0:
#         bits.append(str(n % 2))  # Add remainder as string
#         n = n // 2

#     bits.reverse()  # Reverse the list to get correct order
#     return ''.join(bits)
