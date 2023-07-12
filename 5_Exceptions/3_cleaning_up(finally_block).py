# An finally clause is always executed whether there is an exception or not.

try:
    # file = open(os.path.join())
    file = open("5_Exceptions/1_handling_exceptions.py")
    age = int(input("Age: "))
    xfactor = age / 0
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print(f"No exceptions were thrown. Age: {age}")
finally:
    print("Finally block executed.")
    file.close()
print("Execution continues.")
