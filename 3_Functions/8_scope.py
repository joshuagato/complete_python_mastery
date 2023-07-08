message = "a"


def greet(name):
    message = "b"


def greet_again(name):
    global message
    message = "b"


greet("Josh")
print(message)
greet_again("Josh")
print(message)
