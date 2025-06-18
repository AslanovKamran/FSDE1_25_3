def greeter(language:str):
    def sayHello(name:str):
        if(language == 'en'):
            return f"Hi, {name}"
        elif(language == 'ru'):
            return f"Привет, {name}"
        elif(language == 'az'):
            return f"Salam, {name}"
        else:
            return f"👋 {name}"
    return sayHello

englishGreeter = greeter('ru')
result = englishGreeter("John")
print(result)