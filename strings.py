course = "Python Programming"

print(len(course))  # Length of the string

print(course[0])  # First character of the string

print(course[-1])  # Last character of the string
print(course[0:3])  # First three characters of the string
print(course[0:])  # All characters of the string
print(course[:3])  # First three characters of the string
print(course[:])  # All characters of the string

# Escape sequences
# \"
# \'
# \\
# \n

course_escape = "Python \"programming"
print(course_escape)  # Prints: Python "programming

# formatted strings

first = "Alan"
last = "Poe"
# full = first + " " + last
full = f"{len(first)} {last}"  # f-string formatting
print(full)  # Prints: Alan Poe

# String methods
print(course.upper())  # Converts to uppercase
print(course.lower())  # Converts to lowercase
print(course.find("Pro"))  # Finds the index of the first occurrence of "pro"
print(course.replace("m", "a"))  # Replaces "m" with "a"
print("Pro" in course)  # Checks if "pro" is in the string
print("roe" not in course)  # Checks if "roe" is not in the string
