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


money = False
ticket = True

isLuggageBig = False

time = 15

hasAccess = money or ticket
madeOnTime = time > 6 and time < 12
luggageFits = not isLuggageBig

print(hasAccess and madeOnTime and luggageFits)

print((money or ticket) and not isLuggageBig and (time > 6 and time < 12))
