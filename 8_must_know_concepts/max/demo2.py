numbers_1 = [2, 3, 4, 5, 6, 7]

numbers_2 = [[2, 3], [4, 5], [6, 7]]

result = max(numbers_1, key=sum)
print(result)
# Complain with "TypeError: 'int' object is not iterable"
# Because sum ask for iterable as it's arguments. and
# 2 is passed to it in first iteration, which is an int.

print(max(numbers_2, key=sum))
# Output: [6, 7]
# Will work. Simply because in each iteration sum will return some
# Value and max will do it's magic as beautifully explained by
# @s_gruppetta_ct


my_list = ['Python', 'Java', 'JavaScript', 'C', 'Go']
print(max(my_list, key=sum))
