numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
third = numbers[2]


# NB: The number of variables on the left should be equal to the number of items in the list on the right
first, second, third = numbers

# What if we care about the first two items only?
numbers = [1, 2, 3, 4, 5, 6]
first, second, *others = numbers
print(first)
print(second)
print(others)
print()

# What if we care about the first and last item only
numbers = [1, 2, 3, 4, 5, 6]
first, *others, last = numbers
print(first)
print(last)
print(others)
