point = {"x": 1, "y": 2}
print(point)
point = dict(x=2, y=1)
print(point)

# Get
x = point["x"]
print(x)

# Set
point["x"] = 10
point["z"] = 20
x = point["x"]
print(x)
print(point)

# Accessing non-existing items
if "a" in point:
    print(point["a"])

print(point.get("a"))  # returns None since "a" doesn't exist

# returns 0 (default value we specified) since "a" doesn't exist
print(point.get("a", 0))

# Deleting an existing item
del point["x"]
print(point)

# Iterating over all items in the dictionary
for key in point:
    print(key, point[key])

print()

# Cleaner approach to Iterating over all items in the dictionary
for key, value in point.items():
    print(key, value)
