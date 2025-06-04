def divideTwoNumbers(a,b):
    if(b == 0):
        print("Can't divide by zero")
        return
    
    return a//b

result = divideTwoNumbers(10,0)
print(result)