# List

Python lists are a sequence of data or collections of items. Lists are ordered and mutable data structures (more on this below). Each item in the list has an index, which represents its position in the list. The Python documentation mentions:
> Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).

**Note**: More on homogeneous and heterogenous at the bottom of this tutorial.

## Creating a list in Python

In Python, lists are created using the square bracket notation `[]` and placing comma separated sequence of items. For example, the following code creates a list of even numbers:

```python
even_numbers = [2, 4, 6, 8, 10]
```

The items in the list are separated by commas, and the entire list is enclosed within square brackets. We can use this syntax to create lists of any data type, including strings, booleans, list of lists and other data types.

Here is another example that creates a list of strings:

```python
fruits = ['grape', 'banana', 'mango', 'orange']
```

We can also create an empty list by simply using empty square brackets, like this:

```python
empty_list = []
```

Creating a list of mixed data types:

```python
# A list of mixed data types
mixed = [1, 'grape', 3.14, 'cat', True, (1, 2)]
```

## Quickly Creating a List

### Using range() function

To quickly create a list in Python, we can use the range() function. For example, the following code creates a list of even numbers from 1 to 100:

```python
even_numbers = list(range(1, 101, 2))
```

### Using multiplication (*)

Another way to quickly create a list is to use the multiplication method on the list object. This method creates a new list that contains a specified number of copies of a given item. For example, the following code creates a list with 3 copies of the string "hello world":

```python
greetings = ["hello world"] * 3

# Output: ['hello world', 'hello world', 'hello world']
```

### From string to list

The list method accepts iterable as argument and in Python the strings are iterable so we can do the following to create a list from the string.:

```python
print(list("Hello World!"))

# Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
```

## Indexing

In Programming, indexing refers to the process of accessing individual items in a list by their position, or index. In most of the programming languages the lists are zero-indexed. This means the first item in the list has an index of 0, the second item has an index of 1, and so on.

### Examples of indexing in Python

```python
fruits = ['grape', 'banana', 'mango', 'orange']

# Access the first item in the list (index 0)
first_item = fruits[0]

# Access the second item in the list (index 1)
second_item = fruits[1]

# Access the last item in the list (index 3)
last_item = fruits[3]

# Using negative index also, we can get the last item in the list (index -1)
last_item = fruits[-1]
```

### List-Slicing

Syntax for list-slicing: `list[start:stop:step]`, where `start` is the index of the first item to include in the slice, `stop` is the index of the last item to include in the slice, and `step` is the number of items to skip between each item in the slice.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Methods to copy the list using slicing
# 1. numbers[:]
print(numbers[:])

# 2. numbers[::]
print(numbers[::])

# 3. numbers[0:len(numbers):1]
print(numbers[0:len(numbers):1])

# Creating copy of a list using the copy() method.
print(numbers.copy())
```

More examples of list-slicing

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Reverse a list using slicing
print(numbers[::-1])

# Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

```python
# A list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the first 3 items in the list (index 1, 2, 3)
first_three = numbers[:3]
print(first_three)

# Get the last 3 items in the list (index 8, 9, 10)
last_three = numbers[-3:]
print(last_three)

# Get items 3 through 7 in the list (index 3, 4, 5, 6, 7)
in_between = numbers[2:7]
print(in_between)

# Get items 2 through 10 in the list, skipping every other item (index 1, 3, 5, 7, 9)
alternate = numbers[0:9:2]
print(alternate)
```

## List Concatenation (Adding lists)

Here are few example sof adding lists in Python:

### 1. Using `+` operator

```python
list1 = ['a', 'b', 'c']
list2 = [4, 5, 6]

# Add the lists together
new_list = list1 + list2

# Print the resulting list
print(new_list)  # Output: ['a', 'b', 'c', 4, 5, 6]

# or we can do
list1 += list2
print(list1)    # Output: ['a', 'b', 'c', 4, 5, 6]
#Note: this operation is in-place and calls __iadd__ method.
```

### 2. Using append method

```python
list1 = [1, 2, 3]

# Add the element 4 to the end of the list. list.append(4) is equivalent to list[len(list):] = [4]
list1.append(4)

# Print the resulting list
print(list1)  # Output: [1, 2, 3, 4]
```

### 3. Using extend()

```python
list1 = ['a', 'b', 'c']
list2 = [4, 5, 6]

# Add the lists together. The extend method is in-place and changes the list1 permanently.
list1.extend(list2)
print(list1)
```

### 4. Using `*list1` + `*list2` (For Python >=3.5)

```python
list1 = ['a', 'b', 'c']
list2 = [4, 5, 6]

# Add the lists together
print([*list1, *list2])
```

## Useful Lists Methods

### len()

The len() method is used to determine the length of an iterable (Total number of elements in the list). For example:

```python
# Define a list
my_list = [0, 1, 2, 3, 4, 5]

# Use the len() method to get the length of the list
list_length = len(my_list)

# Print the length of the list
print(list_length)  # Output: 6
```

len() function takes an iterable and return the number of items in a iterable.

### count()

The count() method is used to count the number of times an element appears in a list. For examples:

```python
# Define a list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Use the count() method to count the number of times the element 3 appears in the list
count = my_list.count(3)

# Print the count
print(count)  # Output: 3
```

`count()` method takes a value and returns the number of occurrences of that value.

### sort()

The sort() method is used to sort the items of a list in ascending order. For example:

```python
# Define a list
numbers = [5, 4, 3, 2, 1]

# Using the sort() method to sort the numbers list
numbers.sort()

# Print the sorted list
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

The sort() method sorts the items of the list in ascending order in default. The sort() method is an in-place method, meaning that it modifies the original list and does not return a new list.

```python
numbers = [5, 4, 3, 2, 1]

# assigning the value of 'numbers.sort()' to a variable
sorted_list = numbers.sort()

# Print variable
print(sorted_list)  # Output: None
```

It returns `None`, means it is an in-place operation.

We can also use the `sorted()` function to sort a list. The `sorted()` function returns a new list that is sorted, whereas the sort() method sorts the list in-place. The sorted() function takes the list as an argument and returns a new list that is sorted in ascending order. This can be useful if you want to keep the original list unchanged:

```python
# Define a list
my_list = [5, 4, 3, 2, 1]

# Use the sorted() function to sort the list
sorted_list = sorted(my_list)

# Print the sorted list
print(sorted_list)  # Output: [1, 2, 3, 4, 5]
```

### insert()

The `insert()` method is used to insert an item at a specific position in a list. It takes two arguments: the index of the position where the item is required to be inserted, and the item itself.

```python
# A list of fruits
fruits = ['grape', 'banana', 'mango', 'orange']

# insert the item 'apple' at the third location
fruits.insert(3, 'apple')

print(fruits)
# Output: ['grape', 'banana', 'mango', 'apple', 'orange']
```

After the insert operation on a list, all the items after the inserted item shifts to the right by one index.

While using the `insert()` method on a list, if the value of the index is more than the length of the list, insert acts as the append method. For example:

```python
fruits = ['grape', 'banana', 'mango', 'orange']

# insert the item 'apple' at the 100th location, this value is obviously more than the length of the list.
fruits.insert(100, 'apple')

print(fruits)
# Output: ['grape', 'banana', 'mango', 'orange', 'apple']

# The 'apple ' is inserted at the end of the list, which would be the case if we have used 'append()' method here.
```

The same is the case if the absolute value of the negative index passed is more than the value of the length of the list. In, this case it inserts the item at the beginning of the list.

```python
fruits = ['grape', 'banana', 'mango', 'orange']

# insert the item 'apple' at the -100th location, which is obviously more than the length of the list.
fruits.insert(-100, 'apple')

print(fruits)
# Output: ['apple', 'grape', 'banana', 'mango', 'orange']

# The 'apple ' is inserted at the beginning of the list.
```

This behaviour is a little different from the implementation of the `insert()` method in other programming languages. You can read Guido Van Rossum's explanation of this [here](https://code.activestate.com/lists/python-dev/132599).

### pop()

### remove()

### clear()

### del

### sum()

### max()

### min()

## Flattening Nested Lists

## Unpacking List

## List: All methods

```python
# Print a list of methods used to operate on lists.
# We will use the in-built dir() method for this task.
numbers = [8, 7, 6, 5, 4, 3, 2, 1]
print([item for item in dir(numbers) if not item.startswith('_')])

['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

**Note**: Refer 'Looping over a list' at 'for loop' tutorial here.

According to the Python docs, lists are used to store collection of **homogeneous items**, But a question may arise the list can contain any type of data like `items = ['one', 1, ['one', 'two'], (1, 2), {'one': 1}]`. So, why list is not heterogeneous instead of homogeneous?

The discussion about this can be: [read here](https://stackoverflow.com/questions/5150958/lists-in-python)

In brief, if we explore the discussion we find that The terms "semantic type" and "programmatic type" refer to different aspects of the data types used in programming languages.

The semantic type of a data type refers to the meaning or interpretation of the data that it represents. For example, a semantic type of "date" would indicate that the data represents a date and time value.

The programmatic type of a data type, on the other hand, refers to the specific implementation of the data type in a programming language. This includes things like the internal representation of the data, the operations that can be performed on it, and the specific syntax used to work with the data type in the language.

In short, the semantic type of a data type describes what the data represents, while the programmatic type describes how the data is implemented and used in a specific programming language.
