'''
Continue example: 

From a list of numbers print every number except 5.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 5:
        continue
    print(number)

print("Loop is terminated")
