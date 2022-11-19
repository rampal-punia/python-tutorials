import math

numbers = [3, 4, 5, 6]

# 1: multiply all the items of a list
product = math.prod(numbers)
print(product)
# Output: 360


# 2: in tuple with start argument
numbers = (3, 4, 5, 6)
product = math.prod(numbers, start=2)
print(product)
# Output: 720 (As started with 2 in place of default 1)

# 3: Quickly multiply numbers using Range()
numbers = range(5, 11)
product = math.prod(numbers)
print(product)
# Output: 151200
