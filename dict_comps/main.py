''' Dictionary comprehensions(dict-comps) introduction
'''

# About Dictionary
sportsman = {'Dhyan Chand': 'Hockey',
             'Leander paes': 'Lawn Tennis',
             'Sunil Chhhetri': 'Football',
             'Sachin': 'Cricket'}


# Create a new empty dictionary
sportsman = {}


# Create a new dictionary with normal method
squares = {}
for i in range(10):
    squares[i] = i**2

print(squares)


# Create a new dictionary with dict-comps

squares = {i: i**2 for i in range(10)}
print(squares)

# # Create a new dictionary from a dictionary with dict-comps
sportsman = {'Dhyan Chand': 'Hockey',
             'Leander paes': 'Lawn Tennis',
             'Sunil Chhhetri': 'Football',
             'Sachin': 'Cricket'}

sportsman_s = {k: v for k, v in sportsman.items() if k.startswith('S')}

print(sportsman_s)


# Creating a dictionary using dict-comps, where keys are the numbers
# and the values are the strings

strings = 'abcdefghijklamnop'
strings_dict = {i: strings[i] for i in range(len(strings))}
print(strings_dict)

# # using if conditions in a dict-comp
strings = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
           8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'a', 13: 'm', 14: 'n', 15: 'o', 16: 'p'}

# alphabets with number more than 3
dict1 = {k: v for k, v in strings.items() if k > 3}
print(dict1)

# alphabets with even numbers and more than 3
dict2 = {k: v for k, v in strings.items() if k > 3 if k % 2 == 0}
print(dict2)

# vowels with even numbers and more than 3
dict3 = {k: v for k, v in strings.items() if k > 3 if k %
         2 == 0 if v in ['a', 'e', 'i', 'o', 'u']}
print(dict3)
school = {
    'names': {110: 'sachin', 111: 'virat'},
    'class': {1: 'first', 2: 'second'},
}
dict1 = {i: j for k, v in school.items() for i, j in school[k].items()}
print(dict1)

# for k, v in school.items():
#     print(school[k])
