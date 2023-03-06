import re

string = "abcdcdc"
substring = "cdc"
pattern = f'(?={substring})'
count = len(re.findall(pattern, string))
print(count)
