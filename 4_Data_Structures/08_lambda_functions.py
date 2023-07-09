# lambda parameters:expression

items = [
    ("Product2", 9),
    ("Product1", 14),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
print(items)
