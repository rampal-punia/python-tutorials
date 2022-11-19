"""Python Ternary conditional operators:

Using a conditional operation in a single line
as a switch to get one or another value. 
Ternary specifically means having three inputs values.
"""
# Example: 1
# Simple condition
import time
a = 4
b = 9
max = a if a > b else b
print(max)  # Output: 9

# Example: 2
# Multiple values
time_in_hrs = int(time.strftime("%H"))

greeting = "Good Morning" if 0 < time_in_hrs < 12 else "Good After Noon" \
    if 12 <= time_in_hrs < 18 else "Good Evening"
print(greeting)  # Output: According to the localtime

# Example: 3
# Using in a tuple
# Syntax: (false_value, true_value)[test]
value = (a, b)[a > b]
print(value)    # Output: 4 (test fail)
