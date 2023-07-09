letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

print()

# Getting the index of each item
for letter in enumerate(letters):
    print(letter[0], letter[1])

print()

# Cleaner approach
for index, letter in enumerate(letters):
    print(index, letter)
