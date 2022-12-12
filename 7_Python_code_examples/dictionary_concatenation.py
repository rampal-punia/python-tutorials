'''✨ Python: Adding Two Dictionaries ✨

⚡Different methods to add two dictionaries in Python
'''

# Declaring 2 dictionaries
from itertools import chain
d1 = {"name": "John", "age": 25, "is_active": False}
d2 = {"contact": 12345678, "language": "Python", "experience": 12}

# 1️⃣: Using update()
d1.update(d2)
print(d1)

# 2️⃣: Using **arguments (For Python >= 3.5 )
print({**d1, **d2})

# 3️⃣: Using for loop
d3 = dict()
for d in (d1, d2):
    d3.update(d)
print(d3)

# 4️⃣: using chain from itertools
d3 = dict(chain.from_iterable(d.items() for d in (d1, d2)))
print(d3)

# 5️⃣: using pipe(|) character (For Python >= 3.9.0, PEP-584)
d3 = d1 | d2
print(d3)

_____________________________________________________________________________________________
# Output (In all the cases)
# {'name': 'John', 'age': 25, 'is_active': False, 'contact': 12345678, 'language': 'Python', 'experience': 12}
