'''📝 Example codes used in readme.md (Strings)

✨ Uncomment, Run and Check the output.
'''

### Strings examples ###
# str1 = "Hello"
# str2 = 'John Snow'
# str3 = "12345"
# str4 = "_$%^&*()!-="
# str5 = """
# this is also a string,
# which is expanded in
# multiple line!
# """

# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)

### Concatenating strings ###
# fname = "John"
# lname = "Doe"

# print(fname, lname)
# print(fname + ' ' + lname)
# print("Name: {0} {1}".format(fname, lname))
# print(f"Name: {fname} {lname}")

# # Python > 3.8, We can do:
# print(f"Name: {fname=} {lname=}")
# # This is called: Self-documenting expression with the '=' character.

# Escape Sequencing
# How do we print:
# s = "He said, "I am learning Python Programming language." "

# Method-1: Using combination of single and double quotes.
# s = 'He said, "I am learning Python Programming language." '
# print(s)  # Output: He said, "I am learning Python Programming language."

# # Method-2: Using escape character '\'.
# s = "He said, \"I am learning Python Programming language.\" "
# print(s)  # Output: He said, "I am learning Python Programming language."

# # How to escape a 'escape character'?
# # Using two escape characters.
# s = "I am learning \\Python Programming\\ language"
# print(s)  # Output: I am learning \Python Programming\ language

# New line
# s = "I am learning\n Python Programming language"
# print(s)

# Tab
# s = "I am learning\t Python Programming language"
# print(s)

# Windows path
# filepath = r"C:\dirpath\name_of_file"
# print(filepath)

# filepath = "C:\dirpath\name_of_file"
# print(filepath)

# # Output:
# C: \dirpath
# ame_of_file

# Multiplying strings
# s = "Python" * 5
# print(s)

# length
# s = "I am learning Python Programming language"
# print(len(s))

# useful methods
# s = "I am learning Python Programming language"
# print(s.capitalize())
# print(s.count('o'))
# print(s.endswith('e'))
# print(s.find('z'))
# print(s.isdigit())
# print(s.islower())
# print(s.isnumeric())
# print(s.isprintable())
# print(s.lower())
# print(s.replace('a', 'o'))
# print(s.startswith('k'))
# print(s.title())
# print(s.upper())

### String slicing #
# s = "I am learning Python Programming language"

# # Syntax[start:stop:step]
# print(s[2])         # Output: a

# print(s[-2])         # Output: g

# print(s[0:10])      # Output: I am learn

# print(s[10:25])     # Output: ing Python Prog

# print(s[::2])       # Output: Ia erigPto rgamn agae

# # Reverse the string
# print(s[::-1])      # Output: egaugnal gnimmargorP nohtyP gninrael ma I

### Useful string methods ###
# s = "Learning PYTHON"
# print([item for item in dir(s) if not item.startswith('_')])

lang1 = "Python"
lang2 = "Java"
lang3 = "Ruby"

print(lang1, end=' ')
print(lang2, end=' ')
print(lang3)
