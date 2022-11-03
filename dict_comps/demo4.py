''' Dictionary comprehensions(dict-comps) introduction

Using multiple for loops
'''

school = {
    'names': {110: 'sachin', 111: 'virat'},
    'class': {1: 'first', 2: 'second'},
}

# Output a single dictionary
dict1 = {i: j for k, v in school.items() for i, j in school[k].items()}
print(dict1)
