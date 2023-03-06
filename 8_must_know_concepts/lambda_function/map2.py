'''✨ Python: Map function Vs List Comprehensions. ✨

Example 2:
# ⚡Convert each number of a list into string.
'''

# Method 1️⃣: Using inbuilt 'map function'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(lambda num: str(num), numbers)))
# 👉 Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# ---------------------------------------------------
# Method 2️⃣:  Using List comprehension
squares = [str(num) for num in numbers]
print(squares)
# 👉 Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9']
