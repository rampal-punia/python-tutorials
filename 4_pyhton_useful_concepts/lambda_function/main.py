# Single line, small and anonymous functions.


result = (lambda a, b: a * b)(3, 4)
print(result)

# print((lambda a, b: a * b)(3, 4))

word = "Python"
ord_values = [(letter, ord(letter)) for letter in word]
print(ord_values)

print(list(filter(lambda x: ord(x) > 110, word)))
