try:
    # код, где может возникнуть ошибка
    x = int(input("Введите число: "))
    print(10 / x)
except Exception:
    print("I catched the most common exception. I don't know what it was about but I catched it")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Нужно ввести число.")