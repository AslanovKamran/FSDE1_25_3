# 1. 📊 Максимальная сумма подряд идущих двух чисел

# numbers = [5, 1, 9, 2, 3, 7]

# max_sum = numbers[0] + numbers[1]

# index = 2
# while index < len(numbers)-1:

#     if (numbers[index] + numbers[index + 1] > max_sum):
#         max_sum = numbers[index] + numbers[index + 1]

#     index += 1

# print(max_sum)


# 2 🧮 Чётные и нечётные
# data = [11, 4, 9, 2, 7, 6, 0]

# even = []
# odd = []

# for n in data:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)

# print(even)
# print(odd)


# 3 🔄 Разворот вручную

# original = [1, 2, 3, 4]
# reversed_list = []

# maxIndex = len(original) - 1

# while (maxIndex >= 0):
#     reversed_list.append(original[maxIndex])
#     maxIndex -= 1

# print(original)
# print(reversed_list)


# 4. 🎓 Самый высокий средний балл

# students = [
#     ("Ali", [80, 90, 100]),
#     ("Leyla", [70, 75, 80]),
#     ("Kamran", [90, 90, 90])
# ]

# top_name = ""
# top_avg = 0

# for student in students:

#     name = student[0]
#     grades = student[1]

#     avg = sum(grades) / len(grades)

#     if avg > top_avg:
#         top_avg = avg
#         top_name = name

# print(top_name)
# print(top_avg)


# 5. ✍️ Уникальные отсортированные слова
# text = "python is great and python is easy"
# uniqueWords = list(set(text.split(' ')))
# uniqueWords.sort()
# print(uniqueWords)


# 6. ⚔️ Общие и уникальные интересы

# user1 = {"music", "books", "chess", "football"}
# user2 = {"chess", "movies", "books", "coding"}

# общие интересы = user1 & user2;
# необщие интересы user1 ^ user2;
# список всех хобби user1 | user2;
# интересы, которые есть только у первого пользователя user1 - user2;
# интересы, которые есть только у второго пользователя user2 - user1;

# 7. 🤵 Список студентов и их баллы

# grades = {
#     "Ali": [90, 85],
#     "Leyla": [75, 80],
#     "Kamran": [100, 95]
# }

# top_name = ""
# top_total = 0

# for item in grades.items():
#     name = item[0]
#     scores = item[1]

#     total = sum(scores)
#     avg = total / len(scores)

#     print(f"{name}: {avg}")

#     if total > top_total:
#         top_total = total
#         top_name = name

# print("Студент с наибольшей суммой баллов:", top_name)


# 8. 📈 Самое частое слово

# text = "the the python is good and python is fun and good the"
# words = text.split()

# freq = {}

# for w in words:
#     if w in freq:
#         freq[w] += 1
#     else:
#         freq[w] = 1

# most_common_word = ""
# highest_count = 0

# for item in freq.items():
#     word = item[0]
#     count = item[1]
#     print(f"Word {word} appeared {count} time(s)")
#     if count > highest_count:
#         highest_count = count
#         most_common_word = word


# print(most_common_word)


# 9. 🔄 Инвертировать словарь

# data = {
#     "Ali": "Python",
#     "Leyla": "Java",
#     "Kamran": "Python"
# }

# result = {}

# for item in data.items():
#     name = item[0]
#     lang = item[1]

#     if lang not in result:
#         result[lang] = []

#     result[lang].append(name)

# print(result)
