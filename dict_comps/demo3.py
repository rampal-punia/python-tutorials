''' Dictionary comprehensions(dict-comps) introduction

Using multiple if conditions in a dict-comp.
'''

strings = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
    8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'a', 13: 'm', 14: 'n', 15: 'o', 16: 'p'
}

# alphabets with number more than 3 (One-if condition)
dict1 = {k: v for k, v in strings.items() if k > 3}
print(dict1)

# alphabets with even numbers and more than 3 (Two-if conditions)
dict2 = {k: v for k, v in strings.items() if k > 3 if k % 2 == 0}
print(dict2)

# vowels with even numbers and more than 3 (Three-if conditions)
dict3 = {k: v for k, v in strings.items() if k > 3 if k %
         2 == 0 if v in ['a', 'e', 'i', 'o', 'u']}
print(dict3)

# Well can go for more weird syntax but not advisable (poor code readability)
