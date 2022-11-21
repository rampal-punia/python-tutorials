''' ✨ Python Dictionary:
⚡Why 'get method' is better than 'bracket notation []',
while retrieving the values. '''

employee = {
    'name': 'John Snow',
    'age': 30,
    'language': 'Python'
}

# 👇 Throw KeyError: 'experience_year'.
print(employee["experience_year"])

# 👉 To avoid the keyerror use ⚡'get method'.
# This code will return None without complaining
print(employee.get("experience_year"))
# Output: None

# 👉 Further we can provide a default value to be printed,
# if the key is not found
print(employee.get("experience_year", "Not found!"))
