items = [
    ("Product2", 9),
    ("Product1", 14),
    ("Product3", 12),
]

# Poor way
prices = []
for item in items:
    prices.append(item[1])

print(prices)


# Right: Pythonic way
iterable = map(lambda item: item[1], items)
print(iterable)

# Simplified pythonic way
prices = list(map(lambda item: item[1], items))
print(prices)
