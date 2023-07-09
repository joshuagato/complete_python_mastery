letters = ["a", "b", "c"]

# In C based languages, if d doesn't exist in the list, the returned index is -1
# In Python, it will raise an error and that's the reason for the if check
if "d" in letters:
    print(letters.index("d"))

# If d does not exist in the list, the returned value is 0
print(letters.count("d"))
