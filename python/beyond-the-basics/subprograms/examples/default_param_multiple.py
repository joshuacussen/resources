def greet(name, greeting="Hello", uppercase=False):
    greeting = f"{greeting}, {name}!"
    if uppercase:
        print(greeting.upper())
    else:
        print(greeting)


greet("Sim", "Aloha", True)
greet("Shirley", uppercase=True)
