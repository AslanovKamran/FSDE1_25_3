x = 10
def outer():
    def inner():
        nonlocal x
        x = 5
    inner()
outer()
print(x)