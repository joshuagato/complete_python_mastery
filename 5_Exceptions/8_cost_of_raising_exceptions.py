# When writing your own functions, prefer not to raise exceptions because they come at a cost
# When building an application where performance and scalability are important, then it is better to raise exceptions
#       when you really have to
# A a general rule of thumb, when you want to raise exceptions in your functions, think twice. See if you can handle
#       the situation with a simple if statement. Whether there is a performance difference or not, your code will
#       end up a little bit cleaner. So, raise exceptions if your really have to.

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)
if xfactor is None:
    pass
"""

print("First code: ", timeit(code1, number=10000))
print("Second code: ", timeit(code2, number=10000))
