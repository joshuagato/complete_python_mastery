def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Joshua")
file = open("content.txt", "w")
file.write(message)
