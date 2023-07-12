# An except clause can take multiple exceptions

try:
    age = int(input("Age: "))
    xfactor = age / 0
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print(f"No exceptions were thrown. Age: {age}")
print("Execution continues.")
