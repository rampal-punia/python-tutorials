# Sets

A set is a collection of unique items. Sets are similar to lists, but they do not allow duplicate items and are unordered, which means that the items in a set do not have a specific index or position. Sets are commonly used in Python to remove duplicates from a list or to perform mathematical operations such as union, intersection, and difference.

Python docs on sets:
> Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

## Declaring a set

```python
# We have declared this list with duplicate values of 2, and 3.
duplicate_items = [1, 2, 2, 3, 3, 3]

# Convert the duplicate items list to unique items set using set() method.
unique = set(duplicate_list)
print(unique)

# Output: {1, 2, 3}
```

### Declaring an empty set

```python
empty_set = set()
print(type(empty_set))

# Output: <class 'set'>
```

Note: we can not use empty `{}` to declare a set. Because this is reserved for a **dictionary**.

### Add a new value to the set

```python
# define a set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)   

# Output: {1, 2, 3, 4}
```

### Remove a value from the set

```python
my_set = {1, 2, 3}
my_set.remove(1)
print(my_set)   

# Output: {2, 3, 4}
```

### Check if a value is in the set

```python
my_set = {1, 2, 3}
if 4 in my_set:
    print("4 is found in my_set")

# Output: 4 is found in my_set
```

## Get the Union of two sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Method - 1: union()
set3 = set1.union(set2)
print(set3)     # {1, 2, 3, 4, 5, 6}

# Method - 2: union operator (|)
set3 = set1 | set2
print(set3)     # {1, 2, 3, 4, 5, 6} 

# Output: {1, 2, 3, 4, 5, 6}
```

## Get the Intersection of two sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Method - 1: intersection()
set3 = set1.intersection(set2)
print(set3)     # {3, 4}

# Method - 2: intersection operator(&)
set3 = set1 & set2
print(set3)     # {3, 4}
```

## Get the difference between two sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Method - 1: difference()
set3 = set1.difference(set2)
print(set3)     # {1, 2}

# Method - 2: difference operator(-)
set3 = set1 - set2
print(set3)     # {1, 2}
```

## Get the symmetric difference between two sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Method - 1: symmetric_difference()
set3 = set1.symmetric_difference(set2)
print(set3)     # {1, 2, 5, 6}

# Method - 2: symmetric_difference operator(^)
set3 = set1 ^ set2
print(set3)     # {1, 2, 5, 6}
```

## Get the length of a set

```python
my_set = {0, 1, 2, 3, 4, 5, 6}
print(len(my_set))

# Output: 7
```

Just like list `pop()` and `remove()` also works on sets. But as the sets are unordered we can not get an item using an index().

## Set: All methods

```python
print([item for item in dir(set) if not item.startswith('_')])

# Output:
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```
