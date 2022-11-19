list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']
str1 = 'aeiou'

for val1, val2, val3 in zip(list1, list2, str1):
    print(val1, val2, val3)
