""" This is a basic python script """

course = "Python Programming"

print(len(course))
print(course[0])  # First character
print(course[-1])  # Last character

# First three(3) characters excluding the fourth(4th) which is index 3
print(course[0:3])

print(course[0:])  # From first to last

# First three(3) characters excluding the fourth(4th) which is index 3
print(course[:3])

print(course[:])  # Returns a copy of the original string

first = "Joshua"
last = "Gato"

# full = first + " " + last     # String concatenation
# full = f"{first} {last}"      # Formatted string
full = F"{first} {last}"

print(full)
