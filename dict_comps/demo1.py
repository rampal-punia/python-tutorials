''' Dictionary comprehensions(dict-comps) introduction

Create a new dictionary with the help of dict-comp
'''

# First create a new dictionary with normal method
squares = {}
for i in range(10):
    squares[i] = i**2

print(squares)


# Create a new dictionary with dict-comps
squares = {i: i**2 for i in range(10)}
print(squares)
