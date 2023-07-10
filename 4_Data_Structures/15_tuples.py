point = (1, 2)  # Tuple with two items
point = 1, 2  # Tuple with two items without parentheses
point = 1,  # Tuple with one item
point = 1  # Integer
point = ()  # Empty tuple

# Tuple concatenation
point = (1, 2) + (3, 4)
print(point)

# Tuple repitition
point = (1, 2) * 3
print(point)

# Converting iterables to tuples
point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

# Accessing items in a tuple => You can use the techniques for lists
point = (1, 2, 3)
print(point[0:2])

# Unpacking a tuple
x, y, z = point
print(x, y, z)

if 10 in point:
    print("exists")

# Tuples do not support modification
# point[0] = 10  # Error
