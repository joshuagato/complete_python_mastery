from array import array

# Every object in this array should be of the same type: int
numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0  # You cannot re-set any item to a value of a different type

numbers[0] = 0  # This rather is acceptable
