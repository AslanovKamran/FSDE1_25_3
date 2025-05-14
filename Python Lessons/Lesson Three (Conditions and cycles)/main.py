# print("1 == 1:", 1 == 1)  # 1 == 1: True
# print("1 == 2:", 1 == 2)  # 1 == 2: False
#
# print("1 != 1:", 1 != 1)  # 1 != 1: False
# print("1 != 2:", 1 != 2)  # 1 != 2: True
#
#
# print("1 > 10:", 1 > 10)  # 1 > 10: False
# print("10 > 1:", 10 > 1)  # 10 > 1: True
# print("1 > 1:", 1 > 1)  # 1 > 1: False
#
#
# print("2 < 1:", 2 < 1)  # 2 < 1: False
# print("1 < 2:", 1 < 2)  # 1 < 2: True
# print("1 < 1:", 1 < 1)  # 1 < 1: False
#
#
# print("1 >= 1:", 1 >= 1)  # 1 >= 1: True
# print("1 >= 2:", 1 >= 2)  # 1 >= 2: False
# print("2 >= 1:", 2 >= 1)  # 2 >= 1: True
#
#
# print("1 <= 1:", 1 <= 1)  # 1 <= 1: True
# print("1 <= 2:", 1 <= 2)  # 1 <= 2: True
# print("2 <= 1:", 2 <= 1)  # 2 <= 1: False


# print(bool(0))
# print(bool(1))

# print(bool(''))
# print(bool('Hi'))

# doesStink = False
# isFull = True

# shouldThrow = doesStink or isFull

# print(shouldThrow)


# isRaining = True

# takeAnUmbrella = not isRaining

# print(takeAnUmbrella)


# money = False
# ticket = True

# isLuggageBig = False

# time = 15

# hasAccess = money or ticket
# madeOnTime = time > 6 and time < 12
# luggageFits = not isLuggageBig

# print(hasAccess and madeOnTime and luggageFits)

# print((money or ticket) and not isLuggageBig and (time > 6 and time < 12))


# firstLimit = 1
# secondLimit = 5
# sum = 0

# while firstLimit < secondLimit:
#     print(f"Sum = {sum}; Current number = {firstLimit}")
#     sum = sum + firstLimit
#     firstLimit = firstLimit + 1

# print(sum)


# weekDays = ["Sunday", "Monday", "Tuesday",
#             "Wednesday", "Thursday", "Friday", "Saturday"]

# print(type(weekDays))
# print((weekDays))

# weekDays = ["Sunday", "Monday", "Tuesday",
#             "Wednesday", "Thursday", "Friday", "Saturday"]


# print(weekDays[0])
# print(weekDays[1])
# print(weekDays[2])
# print(weekDays[3])
# print(weekDays[4])
# print(weekDays[5])
# print(weekDays[6])

# print(f'Index = -1; Week day = {weekDays[-1]}')
# print(f'Index = -2; Week day = {weekDays[-2]}')
# print(f'Index = -3; Week day = {weekDays[-3]}')
# print(f'Index = -4; Week day = {weekDays[-4]}')
# print(f'Index = -5; Week day = {weekDays[-5]}')
# print(f'Index = -6; Week day = {weekDays[-6]}')
# print(f'Index = -7; Week day = {weekDays[0]}')

# index = 0


# while index < 7:
#     print(weekDays[index])
#     index+=1


# weekDays[0] = "Понедельник"

# print(weekDays)


# name = "Kamran"

# name[0] = 'k'
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])

# index = 0

# while index <= 5:
#     print(name[index])
#     index +=1


# weekDays = ["Sunday", "Monday", "Tuesday",
#             "Wednesday", "Thursday", "Friday", "Saturday"]

# for day in weekDays:
#     print(day)


# for day in weekDays:
#     print(day)


# for num in 5:
#     print(num)

# for number in range(5):
#     print(number, end=',\t')

# for number in range(2, 21, 2):
#     print(number, end=' | ')

# print()
# print()
# i = 2
# while i <= 20:
#     print(i, end=' -> ')
#     i += 2


# weekDays = ["Monday", "Tuesday", "Wednesday",
#             "Thursday", "Friday", "Saturday", "Sunday"]

# index = 6
# while index >=0:
#     print(weekDays[index])
#     index -=1


rows = 5   # количество строк
cols = 3   # количество столбцов
for i in range(rows):  # Внешний цикл по строкам
    for j in range(cols):  # Внутренний цикл по столбцам
        print("🟦", end=" ")  # Печатаем звёздочку без перехода на новую строку
    print()  # Переход на новую строку после завершения столбцов
