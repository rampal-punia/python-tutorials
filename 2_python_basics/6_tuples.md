# Tuples

A tuple is a data type in Python that represents a sequence of immutable(unchangeable) values. Tuples are similar to lists, but they are enclosed in parentheses and they cannot be modified once they are created. We can access the elements of a tuple using square bracket notation, but we cannot modify the elements of a tuple.

The Python documentation reads:
> Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

## Creating a Tuple

```python
# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
# Output: (1, 2, 3, 4, 5)
```

We can define tuple as a read-only lists.

```python
# The number of vowels are 5 and we don't want this data to change or modified.
# This is a good case for using tuple here.

vowels = ('a', 'e', 'i', 'o', 'u')

print(vowels)
# Output: ('a', 'e', 'i', 'o', 'u')

# Note that it is actually the comma which makes a tuple, not the parentheses.

# It is not the bracket that represents a tuple, but it is the comma between
# two or more items that tells Python hey, this is a tuple declaration. Check below:

my_tuple = 1, 2, 3
print(type(my_tuple))

# Output: <class 'tuple'>

# Similarly if we place a single item but add a comma afterwards it becomes a tuple.

my_tuple = 1,
print(type(my_tuple))

# Output: <class 'tuple'>

# declaring an empty tuple

my_tuple = ()
print(type(my_tuple))

# Or
my_tuple = tuple()
# Output: <class 'tuple'>

# Nested tuple
my_nested_tuple = ((1, 2), (3, 4))
```

## Tuple indexing

We can access the items of a tuple by their index.

```python
my_tuple = (1, 2, 3, 4, 5)

# First element (1)
first_element = my_tuple[0]
print(first_element)

# Second element (2)
first_element = my_tuple[1]
print(first_element)

# Last element (5)
first_element = my_tuple[-1]
print(first_element)
```

## Tuple Concatenation (Adding tuples)

Here are few examples of adding tuples in Python:

### 1. Using `+` operator

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Add the tuples together
t3 = t1 + t2

# Print the resulting list
print(t3)  # Output: (1, 2, 3, 4, 5, 6)
```

So, we have discussed that a tuple is immutable, but look at this interesting behavior:

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1))

t1 += t2
print(t1)    # Output: (1, 2, 3, 4, 5, 6)
```

### The tuple t1 is mutated here. The `+=` assignment operator calls `__iadd__` method, which is an in-place operator and now the value of t1 is changed in-place from (1, 2, 3) to (1, 2, 3, 4, 5, 6), as we can see the output of the last print statement. So what happened there? How the tuple is mutated? Let's find out

### 2. Using `*list1` + `*list2` (For Python >=3.5)

```python
list1 = ['a', 'b', 'c']
list2 = [4, 5, 6]

# Add the lists together
print([*list1, *list2])
```

## Can not modified tuple

## Tuple as records

Tuples as records with no field names.

## Tuple: All Methods

```python
print([item for item in dir(my_tuple) if not item.startswith('_')])

# Output: ['count', 'index']
```

t = (1, 2, [30, 40])
t[2] += [50, 60]

## Tuples are not just constant list

[read here](https://jtauber.com/blog/2006/04/15/python_tuples_are_not_just_constant_lists/)

## Immutability of Tuples depends

The immutability of a tuple only applies to the references contained in it. References in a tuple cannot be deleted or replaced. But if one of those references points to a mutable object, and that object is changed, then the value
of the tuple changes.
