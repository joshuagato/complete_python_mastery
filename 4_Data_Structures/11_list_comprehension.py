items = [
    ("Product2", 9),
    ("Product1", 14),
    ("Product3", 12),
]

prices = [item[1] for item in items]  # equivalent to map
print(prices)

filtered = [item for item in items if item[1] > 10]  # equivalent to filter
print(filtered)
