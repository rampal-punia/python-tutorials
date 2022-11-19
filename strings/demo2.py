# find words in a matrix
# reading forwards of backwards

import re

words = ['holy', 'grail', 'monty', 'python',
         'life', 'of', 'brian', 'fool', 'rain']
matrix = ['nlifeloofw', 'liarggoyloh',
          'oanairbens', 'troeasonst', 'swgndmkdhr']

found, not_found = [], []
for word in words:
    if re.compile(word).search('|'.join(matrix)) or re.compile(word[::-1]).search('|'.join(matrix)):
        found.append(word)
    else:
        not_found.append(word)

print("Found: ", found)
print("Not Found: ", not_found)
