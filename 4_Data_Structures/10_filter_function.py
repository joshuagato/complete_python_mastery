items = [
    ("Product2", 9),
    ("Product1", 14),
    ("Product3", 12),
]

iterable = filter(lambda item: item[1] > 10, items)
print(iterable)

items = list(filter(lambda item: item[1] > 10, items))
print(items)
