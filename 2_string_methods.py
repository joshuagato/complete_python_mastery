""" This is a basic python script """
course = "  Python programming   "

course_capital = course.upper()
course_small = course.lower()
course_capitalize = course.title()
course_strip = course.strip()
course_left_strip = course.lstrip()
course_right_strip = course.rstrip()

# Returns the index if the character(s) exist(s)
course_find_existing = course.find("p")
course_find_existing_2 = course.find("pro")

# Doesn't exist so should return -1
course_find_non_existing = course.find("Pro")

course_replace = course.replace('p', 'j')

course_check_existence = "pro" in course    # Returns a boolean
course_check_non_existence = "swift" not in course    # Returns a boolean

print({course})
print(course_capital)
print(course_small)
print(course_capitalize)
print({course_strip})
print(course_left_strip)
print(course_right_strip)
print(course_find_existing)
print(course_find_non_existing)
print(course_replace)
print(course_check_existence)
print(course_check_non_existence)
