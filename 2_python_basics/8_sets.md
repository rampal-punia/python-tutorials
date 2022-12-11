# Sets

A set is a collection of unique items. Sets are similar to lists, but they do not allow duplicate items and are unordered, which means that the items in a set do not have a specific index or position. Sets are commonly used in Python to remove duplicates from a list or to perform mathematical operations such as union, intersection, and difference.

Python docs on sets:
> Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

## Declaring a set

```python
# We have declared this set with duplicate values of 2, and 3, but only one copy of each value
# will get printed out.
my_set = {1, 2, 2, 3, 3, 3}

# Print the set
print(my_set)   # Output: {1, 2, 3}
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
my_set = {1, 2, 2, 3, 3, 3}
my_set.add(4)
print(my_set)   

# Output: {1, 2, 3, 4}
```

### Remove a value from the set

```python
my_set = {1, 2, 2, 3, 3, 3}
my_set.remove(1)
print(my_set)   

# Output: {2, 3, 4}
```

### Check if a value is in the set

```python
my_set = {1, 2, 2, 3, 3, 3}
if 4 in my_set:
    print("4 is found in my_set")

# Output: 4 is found in my_set
```

### Union of two sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.union(set2)
print(set3)  

# Output: {1, 2, 3, 4, 5, 6}
```

## Set: All methods

```python
print([item for item in dir(set) if not item.startswith('_')])

# Output:
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```

##
