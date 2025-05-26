listOne = [10, 5, -3, -4, 4, 2]

indexesOfPositive = []
positiveNumbers = []

for element in listOne:
    if (element > 0):
        indexesOfPositive.append(listOne.index(element))
        positiveNumbers.append(element)

print(indexesOfPositive)
positiveNumbers.sort()
