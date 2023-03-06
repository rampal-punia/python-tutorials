''' Dictionary comprehensions(dict-comps) introduction

Create a new modified dictionary from existing dictionary.
'''
# Example 1
# Declare a dictionay
sportsman = {
    'Dhyan Chand': 'Hockey',
    'Leander paes': 'Lawn Tennis',
    'Sunil Chhhetri': 'Football',
    'Sachin': 'Cricket'
}

# Create a new dictionary with key starting with "S"
sportsman_s = {k: v for k, v in sportsman.items() if k.startswith('S')}
print(sportsman_s)

# Example 2
strings = 'abcdefghijklamnop'
strings_dict = {i: strings[i] for i in range(len(strings))}
print(strings_dict)
