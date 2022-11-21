list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']
str1 = 'aeiou'

# To get a list
print(list(zip(list1, list2, str1)))


# # Suppose given
# numbers = [(3, 2), (3, 3), (3, 4), (3, 5)]

# # Required: 3², 3³, 3⁴, 3⁵

# nums, powers = zip(*numbers)
# print(nums)
# print(powers)

# print(list(map(pow, nums, powers)))
