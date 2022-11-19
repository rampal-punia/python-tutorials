# find words in a matrix
# reading forwards of backwards

import re

words = ['holy', 'grail', 'python', 'life', 'of', 'brian', 'fool', 'rain']
matrix = ['nlifeloofw',
          'liarggoyloh',
          'oanairbens',
          'troeasonst',
          'swgndmkdhr',
          'python'
          ]

print(re.IGNORECASE)
# search_list = ['one', 'two', 'there']
# long_string = 'some one long two phrase three'
# re.IGNORECASE is used to ignore case
# for word in words:
#     if re.compile(word, re.IGNORECASE).search('|'.join(matrix)):
#         # if re.compile('|'.join(words), re.IGNORECASE).search('|'.join(matrix)):
#         print("Found")
#     else:
#         print("Not found")

# words = ['holy', 'grail', 'python', 'life', 'of', 'brian', 'fool', 'rain']

# matrix = ['nlifeloofw',
#           'liarggoyloh',
#           'oanairbens',
#           'troeasonst',
#           'swgndmkdhr',
#           'python'
#           ]

# for obj in matrix:
#     for i in range(len(words)):
#         if obj.find(words[0][::-1]):
#             print(words[0])
#             break


# if any(word in matrix for word in words):
#     print("yes")
