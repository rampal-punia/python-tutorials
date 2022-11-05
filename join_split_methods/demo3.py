"""
🐍 Python os.path.split() method.
    Takes a pathlike object as input and return a tuple "(head, tail)" where 
    "tail" is everything after the final slash(/).

Syntax:
    os.path.split(filepath)
    
"""
import os

# 🎯Example 1:
result = os.path.split(
    "/home/CodingMantras/PythonTutorials/join_split_methods/demo3.py")

print(result)
# Output: ('/home/CodingMantras/PythonTutorials/join_split_methods', 'demo3.py')

# 🎯Example2 : Joining list str elements with a hyphen.
result = os.path.split(
    "/home/CodingMantras/PythonTutorials")

print(result)
# Output: ('/home/CodingMantras', 'PythonTutorials')

# 🚀 @CodingMantras 🚀
# See you soon... Till then keep improving...🤝
