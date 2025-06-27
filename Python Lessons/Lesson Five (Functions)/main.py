import time
import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log(func):
    def wrapper(*args, **kwargs):
        print("="*20)
        print("Log 📝:", end='\n\n')
        functionName = func.__name__
        print(f"Function #{functionName} call time: {datetime.datetime.now()}")
        print(f"Function took {args} positional arguments")
        print(f"Function took {kwargs} named arguments")
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        if (result is not None):
            print(f"Function result is {result}")
        print(
            f"{bcolors.OKGREEN}⏱ Execution time: {(endTime - startTime):.6f}{bcolors.ENDC}")
        print("\n", "="*20)
    return wrapper


def my_sum(*args):
    total = 0
    for number in args:
        total += number
    return total


logged = log(my_sum)
logged(3, 2, 1)

# logged = log(my_sum)
# logged(45184, 876454558, 4687941)
