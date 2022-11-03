'''
Continue example: 

From the texts "A quick brown fox jumps over the lazy dog" 
print everything except the letter 's'.
'''

string = "A quick brown fox jumps over the lazy dog"

for letter in string:
    if letter == 's':
        continue
    print(letter)

print("Loop is terminated")
