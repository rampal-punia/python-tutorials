"""🐍 Python String Split() method.
Splits a string based on separator as the delimiter string and returns a list.

👉Example separators:
(' '), ('-'), ('/ '), (', '), 

👉maxsplit:
Maximum number of splits to do. -1 (the default value) means no limit.
"""

# 🎯Example1: Using default separator
string = "Python is a wonderful programming language"
print(string.split())
# Output: ['Python', 'is', 'a', 'wonderful', 'programming', 'language']

# 🎯Example2: Using ('-') as separator
string = "Python-is-a-wonderful-programming-language"
print(string.split("-"))
# Output: ['Python', 'is', 'a', 'wonderful', 'programming', 'language']

# 🎯Example3: Using (', ') as separator, and specifying maxsplit
string = "Python, is, a, wonderful, programming, language"
print(string.split(", ", maxsplit=3))
# Output: ['Python', 'is', 'a', 'wonderful, programming, language']
# notice only upto 3 words the split is applied rest string is as it was
# but returned as an item of a list.

# 🚀 @CodingMantras 🚀
# See you soon... Till then keep improving...🤝
