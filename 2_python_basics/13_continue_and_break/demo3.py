'''
Break example: 

from the texts "A quick brown fox jumps over the lazy dog" print up to 's'.
'''

string = "A quick brown fox jumps over the lazy dog"

for letter in string:
    if letter == 's':
        break
    print(letter)

print("Loop is terminated")
