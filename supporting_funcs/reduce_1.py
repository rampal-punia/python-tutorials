'''Reduce function example: Get result of each element in a list.
'''
from functools import reduce

numbers = [2, 3, 4, 5, 6, 7]

result = reduce(lambda a, b: a*b, numbers)

print(result)
