import time

# Example: 1
# Simple condition
a = 4
b = 9

max = a if a > b else b
print(max)


# Example: 2
# Multiple values
time_in_hrs = int(time.strftime("%H"))

greeting = "Good Morning" if 0 < time_in_hrs < 12 else "Good After Noon" if 12 <= time_in_hrs < 18 else "Good Evening"
print(greeting)

# Example: 3
# Using in a tuple
# Syntax: (false_value, true_value)[test]
value = (a, b)[a > b]
print(value)
