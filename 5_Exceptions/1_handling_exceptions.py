try:
    age = int(input("Age: "))
    xfactor = age / 0
    pass
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
except ZeroDivisionError as ex:
    print("Age cannot be zero.")
    print(ex)
    print(type(ex))
else:
    # print(f"No exceptions were thrown. Age: {age}")
    print(f"No exceptions were thrown.")
print("Execution continues.")
