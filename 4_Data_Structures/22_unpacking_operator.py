numbers = [1, 2, 3]
print(numbers)
print(*numbers)  # The unpacking operation

values = list(range(5))
print(values)

# The unpacking operation
values = [*range(5)]
print(values)

values = [*range(5), *"Hello"]
print(values)

# Using the unpacking operator *, we can combine multiple lists
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

# using the unpacking operator, we can unpack dictionaries using **
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 3}
print(combined)

# If we have multiple items with the same key, the last value will be used; hence x => 10 and not 1
