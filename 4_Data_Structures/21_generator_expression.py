from sys import getsizeof

# Tuple comprehension results in a generator object: which is memory efficient
values = (x * 2 for x in range(1000))
# returns 208 (value may differ on a different machine)
print("gen: ", getsizeof(values))

values = (x * 2 for x in range(10000000))
# returns 208 (value may differ on a different machine)
print("gen: ", getsizeof(values))

# Since generator expression don't store values in memory, when we try accessing the length of the generator
# we get an error
# print(len(values)) # raises an error

# List comprehension is memory inefficient as compared to tuple comprehension
values = [x * 2 for x in range(1000)]
# returns 8856 (value may differ on a different machine)
print("gen: ", getsizeof(values))

values = [x * 2 for x in range(10000000)]
# returns 89095160 (value may differ on a different machine)
print("gen: ", getsizeof(values))
