# The with statement is used to automatically release external resources

try:
    with open("5_Exceptions/1_handling_exceptions.py") as file, open("5_Exceptions/4_the_with_statement_2.py") as target:
        # print(file.read())
        print("File opened.")
    age = int(input("Age: "))
    xfactor = age / 0
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print(f"No exceptions were thrown. Age: {age}")
print("Execution continues.")
