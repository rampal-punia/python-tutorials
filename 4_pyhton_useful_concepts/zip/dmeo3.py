'''📝 Python Zip with Map function

✨ Required: 3², 3³, 3⁴, 3⁵
'''

# Suppose given
numbers = [(3, 2), (3, 3), (3, 4), (3, 5)]
nums, powers = zip(*numbers)

print(list(map(pow, nums, powers)))
