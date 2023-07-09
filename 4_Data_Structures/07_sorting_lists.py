numbers = [3, 51, 2, 8, 6]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

items = [
    ("Product2", 9),
    ("Product1", 14),
    ("Product3", 12),
]

items.sort()  # this has no effect since Python does not know how to sort such a complex list


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
