high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")


# Chaining comparison operators
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
