'''📝 Example codes used in readme.md (Python Basics)

✨ Uncomment, Run and Check the output
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Method - 1: symmetric_difference()
set3 = set1.symmetric_difference(set2)
print(set3)     # {1, 2}

# Method - 2: symmetric_difference operator(^)
set3 = set1 ^ set2
print(set3)     # {1, 2}
