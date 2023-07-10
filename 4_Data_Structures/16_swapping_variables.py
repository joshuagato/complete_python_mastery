x = 10
y = 11

# When swapping we need a third variable; in this case z
z = x
x = y
y = z

print("x: ", x)
print("y: ", y)

print()

x = 10
y = 11

# Swapping the Pythonic way
x, y = y, x

print("x: ", x)
print("y: ", y)
