# Set comprehension
values = {x * 2 for x in range(5)}
print(values)

# Dictionary comprehension: Manual approach
values = {}

for x in range(5):
    values[x] = x * 2

print(values)

# Dictionary comprehension: Pythonic approach
values = {x: x * 2 for x in values}
print(values)
