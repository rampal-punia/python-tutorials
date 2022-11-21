'''✨ Python: Map function Vs List Comprehensions.

Example 1:
⚡Convert each number of a list into its square. 
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Method 1️⃣: Using inbuilt 'map function'
print(list(map(lambda num: pow(num, 2), numbers)))
# 👉 Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# ---------------------------------------------------
# Method 2️⃣: Using List comprehension
squares = [pow(num, 2) for num in numbers]
print(squares)
# 👉 Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
