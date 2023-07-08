def multiply(*numbers):
    print(numbers)


multiply(1, 2, 3, 4)


def multiply_again(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply_again(1, 2, 3, 4))
