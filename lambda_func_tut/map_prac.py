'''Map function example to add 5 to every element of a list.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mapped_numbers = map(lambda x: x+5, numbers)

print(mapped_numbers)
