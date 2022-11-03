'''
Break example: 

from a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9] print every number up to '5'.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 5:
        break
    print(num)

print("Loop is terminated")
