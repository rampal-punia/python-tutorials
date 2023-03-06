# Dictionaries

A dictionary is a data type that represents a collection of keys and values. Dictionaries are also known as associative arrays or hash maps. Dictionaries are similar to lists, but they are indexed by keys instead of integers. Each key in a dictionary is associated with a value, which can be of any data type.

Here is an example of defining and using a dictionary in Python:

```python
# Define a dictionary with three keys and their associated values
person = {"name": "John", "age": 25, "contact": 12345678}

# Access the values in the dictionary using their keys
print(person["name"])          # Output: "Alice"
print(person["age"])           # Output: 25
print(person["contact"])       # Output: 12345678

# Add a new key-value pair to the dictionary
person["gender"] = "Male"

print(person)
# Output: {'name': 'John', 'age': 25, 'contact': 12345678, 'gender': 'Male'}

# Remove a key-value pair from the dictionary using the del keyword
del person["contact"]
print(person)
# Output: {'name': 'John', 'age': 25, 'gender': 'Male'}
```

Defining an empty dictionary.

```python
# Method-1
empty_dict = {}

# Method-2
empty_dict = dict()

print(empty_dict)           # {}
print(type(empty_dict))     # <class 'dict'>
```

## Different ways of declaring a dictionary

```python
# Method-1 using {} with key:value
d1 = {"name": "John", "age": 25, "is_active": True}

# Method-2 using dict() with keyword arguments as key:value
d2 = dict(name="John", age=25, is_active=True)

# Method-3 using dict() with tuple as a key:value pair
d3 = dict([("name", "John"), ("age", 25), ("is_active", True)])

# The dict() constructor builds dictionaries directly from sequences of key-value pairs.

# Method-4 zipping two lists together as key:value
l1 = ["name", "age", "is_active"]
l2 = ["John", 25, True]
d4 = dict(zip(l1, l2))

print(d4)       # {'name': 'John', 'age': 25, 'is_active': True}

print(d1 == d2 == d3 == d4)     # True
```

### Using dict-comprehension

```python
squares = {x: x**2 for x in range(10)}
print(squares)

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### Get the list of all the keys

Get all the keys of a dictionary using `dict.keys()`.

For example:

```python
# Declare a dictionary
d1 = {"name": "John", "age": 25, "is_active": True}

keys = d1.keys()
print(keys)         # dict_keys(['name', 'age', 'is_active'])

# Or we can do
print(list(keys))   # ['name', 'age', 'is_active']
```

### Get the list of all the values

Similarly, we can use `dict.values()` to get all the values of the dictionary.

```python
# Declare a dictionary
d1 = {"name": "John", "age": 25, "is_active": True}

values = d1.values()
print(values)         # dict_values(['John', 25, True])

# Or we can do
print(list(values))   # ['John', 25, True]
```

### Get the list of all the items

To get all the items(keys & values) of a dictionary we use `dict.items()`.

For example:

```python
d1 = {"name": "John", "age": 25, "is_active": True}

all_items = d1.items()
print(all_items)
# dict_items([('name', 'John'), ('age', 25), ('is_active', True)])

# Or we can do
print(list(all_items))   
# [('name', 'John'), ('age', 25), ('is_active', True)]
```

## [] vs get()

```python
employee = {
    'name': 'John Snow',
    'age': 30,
    'language': 'Python'
}

# Throw KeyError: 'experience_year'.
# print(employee["experience_year"])

# To avoid the key-error we can use: 
# Method - 1: if statement

if "experience_year" in employee:
    print(employee["experience_year"])

# Method - 2: use 'get method'.
# This code will return None without complaining
print(employee.get("experience_year"))
# Output: None

# Further we can provide a default value to be printed,
# if the key is not found
print(employee.get("experience_year", "Not found!"))
```

## update an item of a dictionary

Using `update()` method we can update an item of the existing dictionary.

```python
employee = {
    'name': 'John Snow',
    'age': 30,
    'language': 'Python'
}

employee.update(name="John Doe")
# update take a key word argument
print(employee)

# Output: {'name': 'John Doe', 'age': 30, 'language': 'Python'}
```

## del

Use del method to delete an item from a dictionary.

```python
employee = {
    'name': 'John Snow',
    'age': 30,
    'language': 'Python'
}

print(employee)
# {'name': 'John Snow', 'age': 30, 'language': 'Python'}

del employee['age']
print(employee)
# {'name': 'John Snow', 'language': 'Python'}
```

## Adding two dictionaries

```python
d1 = {"name": "John", "age": 25, "is_active": False}
d2 = {"contact": 12345678, "language": "Python", "experience": 12}

# Method -1 : Using update()

d1.update(d2)
print(d1)

# Output
# {'name': 'John', 'age': 25, 'is_active': False 'contact': 12345678, 'language': 'Python', 'experience': 12}

# Method -2: Using **arguments (For Python >= 3.5 )
print({**d1, **d2})

# Output
# {'name': 'John', 'age': 25, 'is_active': False 'contact': 12345678, 'language': 'Python', 'experience': 12}

# Method - 3: Using for loop
d3 = dict()

for d in (d1, d2):
    d3.update(d)

print(d3)
# Output
# {'name': 'John', 'age': 25, 'is_active': False 'contact': 12345678, 'language': 'Python', 'experience': 12}

# Method - 4: using chain from itertools
from itertools import chain
d3 = dict(chain.from_iterable(d.items() for d in (d1, d2)))
print(d3)
# Output
# {'name': 'John', 'age': 25, 'is_active': False 'contact': 12345678, 'language': 'Python', 'experience': 12}

# Method - 5: using pipe(|) character (For Python >= 3.9.0, PEP-584)
d3 = d1 | d2
print(d3)
# Output
# {'name': 'John', 'age': 25, 'is_active': False 'contact': 12345678, 'language': 'Python', 'experience': 12}
```

Note: If a key is present in both of the dictionary, the later one will overwrite the first one.

For example:

```python
d1 = {"name": "John", "age": 25, "is_active": False}
d2 = {"age": 35, "language": "Python", "experience": 12}

d3 = {**d1, **d2}

print(d3)
# Output:
# {'name': 'John', 'age': 35, 'is_active': False, 'language': 'Python', 'experience': 12}
```

## Looping Over a dictionary(for loop tutorial link)

## Dictionary: All methods

```python
print([item for item in dir(dict) if not item.startswith('_')])
# Output
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```
