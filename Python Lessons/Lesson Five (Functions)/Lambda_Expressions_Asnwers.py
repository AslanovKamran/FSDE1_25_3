# ✅ 1. Отфильтровать только положительные числа
# numbers = [-3, -1, 0, 2, 4]
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# print(positive_numbers)  # ➝ [2, 4]


# ✅ 2. Получить длины строк
# words = ["hi", "hello", "world"]
# lengths = list(map(lambda word: len(word), words))
# print(lengths)  # ➝ [2, 5, 5]


# ✅ 3. Округлить числа до целого
# Дан список дробных чисел. С помощью map() и lambda округли их до ближайшего целого.
# Вход:
# [3.2, 4.7, 1.5, 9.9]

# Ожидаемый результат:
# [3, 5, 2, 10]

# numbers = [3.2, 4.7, 1.5, 9.9]
# rounded = list(map(lambda x: round(x), numbers))
# print(rounded)  # ➝ [3, 5, 2, 10]


# # ✅ 4. Чётные числа → удвоить
# nums = [1, 2, 3, 4]
# even = list(filter(lambda x: x % 2 == 0, nums))
# even_doubled = list(map(lambda x: x*2, even))
# print(even_doubled)  # ➝ [4, 8]

# ✅ 5. Оставить строки с чётной длиной
# strings = ["one", "four", "six", "twelve"]
# even_length = list(filter(lambda s: len(s) % 2 == 0, strings))
# print(even_length)  # ➝ ["four", "twelve"]

# ✅ 6. Отфильтровать числа, которые являются квадратами целых чисел
# nums = [1, 2, 3, 4, 5, 9, 10, 16]
# perfect_squares = list(filter(lambda x: (x ** 0.5) ** 2 == x, nums))
# print(perfect_squares)  # ➝ [1, 4, 9, 16]

# import math

# nums = [1, 2, 3, 4, 5, 9, 10, 16]
# perfect_squares = list(filter(lambda x: math.isqrt(x) ** 2 == x, nums))
# print(perfect_squares)  # ➝ [1, 4, 9, 16]
