x = input("X: ")

y = int(x) + 1

print(f"x: {x}, y: {y}")

print(type(x))

int(x)
float(x)
bool(x)
str(x)

# Falsy
print(bool(0))
print(bool(""))
print(bool(None))

print()

# Truthy
print(bool(1))
print(bool(-1))
print(bool(5))
print(bool("False"))
