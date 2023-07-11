numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)

print(uniques)

second = {1, 5}
# second.add(5)
# second.remove(5)
print(len(second))
print(second)

union = uniques | second
print(union)

intersection = uniques & second
print(intersection)

difference = uniques - second
print(difference)

symmetric_difference = uniques ^ second
print(symmetric_difference)

# Sets are not ordered therefore if you try accessing an item using the square bracket notation, it raises an exception
# first_item = uniques[0]  # This is an error

if 1 in uniques:
    print("1 is in the set")
