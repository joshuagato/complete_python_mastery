letters = ["a", "b", "c", "d", "e", "f"]


# Add
letters.append("g")  # Adds g to the end of the list
letters.insert(0, "-")  # Adds - to the index 0 or beginning of the list
print(letters)

print()

# Remove
letters.pop()  # Removes one item from the end of the list
letters.pop(0)  # Removes the item at index 0 of the list

del letters[0]  # Removes the item at index 0 of the list

# Removes a range of items in the list; from index 0 (first) to index 2 (third)
del letters[0:3]
print(letters)

print()

# Delete all items in the list
letters.clear()
print(letters)
