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
```

Note: It is actually the comma which makes a tuple, not the parentheses. It means that it is not the bracket that represents a tuple, but it is the comma between two or more items that tells Python hey, this is a tuple declaration. Check below:

```python
my_tuple = 1, 2, 3
print(type(my_tuple))

# Output: <class 'tuple'>

# Similarly if we place a single item but add a comma afterwards it becomes a tuple.

my_tuple = 1,
print(type(my_tuple))

# Output: <class 'tuple'>
```

### Declaring an empty tuple

```python
my_empty_tuple = ()
print(type(my_empty_tuple))

# Or
my_empty_tuple = tuple()
# Output: <class 'tuple'>
```

### Using tuple() function to convert a list into tuple

```python
a_list = [1, 2, 3, 4, 5]

a_tuple = tuple(a_list)
print(a_tuple)
# Output: (1, 2, 3, 4, 5)
```

### Declaring a Nested Tuple

```python
my_nested_tuple = ((1, 2), (3, 4))
```

## Quickly Creating a Tuple

### Using range() Function

```python
my_tuple = tuple(item for item in range(1, 100))
print(my_tuple)

# Output: (1, 2, 3, 4, ..., 99, 100)
```

Note: Using the bracket notation only (without the tuple()) will give a generator object and not a tuple.

For example:

```python
my_tuple = (item for item in range(1, 100))
print(my_tuple)

# Output: <generator object <genexpr> at 0x7fd43cae0b30>
```

### Using Multiplication

```python
my_tuple = (1, 2) * 5
print(my_tuple)

# Output: (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)

```

## Tuple Indexing

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

## Tuples can not be Modified

If we try to modify the tuple we get a `TypeError`. For example:

```python
my_tuple = (1, 2, 3, 4, 5)

# Modify first element from 1 to 10
my_tuple[0] = 10
print(my_tuple)

# Output: TypeError: 'tuple' object does not support item assignment
```

## Tuple Unpacking

```python
my_tuple = (1, 2, 3)

first, second, third = my_tuple
print(first, second, third)
# Output: 1 2 3

# The number of variables must be equal to the elements in a tuple
# or we get an error(TypeError).
my_tuple = (1, 2, 3, 4, 5)
first, second, third = my_tuple
print(first, second, third)

# Output: ValueError: too many values to unpack (expected 3)
```

Use `*` in this situation, it will accumulate the rest of the items.

For example:

```python
my_tuple = (1, 2, 3, 4, 5)

first, *middle, last = my_tuple

print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5
```

## Getting two or more outputs from a function

A function can return more than one value. These values are comma separated hence by default they are treated as a tuple.

```python
# A function that returns two values

def my_func():
    return 2, 3

# Check the type of the output. It is a tuple.
print(type(my_func()))
# Output: <class 'tuple'>

# Unpacking these two values
x, y = my_func()
print(x)
print(y)

# Output:
2
3
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

t1 += t2
print(t1)    # Output: (1, 2, 3, 4, 5, 6)
```

#### The tuple t1 is mutated here. The `+=` assignment operator calls `__iadd__` method, which is an in-place operator and now the value of t1 is changed in-place from (1, 2, 3) to (1, 2, 3, 4, 5, 6), as we can see the output of the last print statement. So what happened there? How the tuple is mutated? Let's find out

If we check the id() of t1 first and after the merging with t2 we find out that both are different.

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1))       # 140600311167616

t1 += t2
print(t1)    # Output: (1, 2, 3, 4, 5, 6)
print(id(t1))       # 140600311575552
```

Therefore the original t1 is not modified but we got the copy of the original tuple.

But interestingly, if we try to copy the tuple with slicing operation, both the variables refer to the same tuple object. For example:

```python
t1 = (1, 2, 3)
print(id(t1))       # 139766396087104

t2 = t1[:]
print(id(t1))       # 139766396087104
print(id(t2))       # 139766396087104

print(t2 is t1)     # True
```

#### And if we create two similar tuples from scratch they have different locations in the memory. For example

```python
# Use Python Console not Code editor for this
t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(id(t1))       # 140142727341568
print(id(t2))       # 140142727340480

print(t2 is t1)     # False
print(t2 == t1)     # True
```

### 2. Using `*tuple1` + `*tuple2` (For Python >=3.5)

```python
t1 = ('a', 'b', 'c')
t2 = (4, 5, 6)

# Add the lists together
print((*t1, *t2))

# Output: ('a', 'b', 'c', 4, 5, 6)
```

## Tuple as records

Tuples are used as records with no field names. As, a tuple is a sequence of values, they are fixed in size and cannot be modified. Therefore, tuples are often used to represent records, such as a student's name, age, and roll number.

For example:

```python
# Define a tuple representing a student's name, age and roll_num
student = ("John", 15, 10)

# Access the values in the tuple using their index
print(student[0])  # Output: "John"
print(student[1])  # Output: 15
print(student[2])  # Output: 10

# You can also unpack the values in the tuple into separate variables
name, age, roll_num = student
print(name)         # Output: "John"
print(age)          # Output: 25
print(roll_num)     # Output: 10
```

## Tuple: All Methods

```python
print([item for item in dir(tuple) if not item.startswith('_')])

# Output: ['count', 'index']
```

t = (1, 2, [30, 40])
t[2] += [50, 60]

## Tuples are not just constant list

[read here](https://jtauber.com/blog/2006/04/15/python_tuples_are_not_just_constant_lists/)

## Immutability of Tuples depends

The tuple are immutable data structure. Therefore references in a tuple cannot be deleted or replaced. But if one of those references points to a mutable object/data structure, the value of the tuple may change.

For example:

```python
t = (2, 3, [4, 5])
t[2].append(6)
print(t)

# Output: (2, 3, [4, 5, 6])
```

So, we can see here, the tuple `t` is mutated. The reason behind this is; `t[2]` refers to a mutable list object. Therefore we are changing the list object which is refereed by the `t[2]`.
