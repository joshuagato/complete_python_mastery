letters = ["a", "b", "c", "d"]
numbers = list(range(20))

matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
chars = list("Hello World")
chars_length = len(chars)


print(letters[0])  # First Item
print(letters[-1])  # First Item from the end of the list

letters[0] = "A"
print(letters)

# Returns a new list from first three items in the original list
print(letters[0:3])
print(letters[:3])

# From beginning to the end (using the length of the list as the end)
print(letters[0:])

print(letters[:])  # Returns a copy of the original list

print(letters[::2])  # Returns a copy of the original list in steps of 2
print(numbers)
print(numbers[::2])  # Returns a copy of the original list in steps of 2
print(numbers[::-1])  # Returns a copy of the list in reverse order
