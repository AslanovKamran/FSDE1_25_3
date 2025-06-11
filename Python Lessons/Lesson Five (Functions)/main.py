def addElementToTheEnd(myList, newElement):
    print("If of parameter  ", id(myList))
    myList.append(newElement)


numbers = [1, 2, 3]
print("Id of original   ", id(numbers))
addElementToTheEnd(numbers, 4)

print(numbers)
