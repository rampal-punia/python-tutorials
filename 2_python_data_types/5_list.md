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

Here are few examples of adding lists in Python:

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
# __iadd__ mutates the original list(in-place), whereas __add__ returns a new list.
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

### len()

The len() is an in-built function in python to get the length of an iterable. For example:

```python
# Define a list
my_list = [0, 1, 2, 3, 4, 5]

# Use the len() method to get the length of the list
list_length = len(my_list)

# Print the length of the list
print(list_length)  # Output: 6
```

len() function takes an iterable and return the number of items in a iterable.

## Useful Lists Methods

|Name of the method|Description|
|--------------|--------------------|
|append(x)| Adds an item (x) to the end of the list.|
|extend(iterable)| Adds all the items from an iterable (e.g. list, tuple, string) to the end of the list.|
|insert(i, x)| Inserts an item (x) at a given position (i) in the list.|
|remove(x)| Removes the first item from the list that has the value x.|
|pop([i])| Removes and returns the item at the given position (i) in the list. If no position is specified, it removes and returns the last item.|
|clear()| Removes all items from the list.|
|index(x)| Returns the index of the first item in the list that has the value x.|
|count(x)| Returns the number of times x appears in the list.|
|sort()| Sorts the items in the list in ascending order.|
|reverse()| Reverses the order of the items in the list.|
|copy()| Returns a shallow copy of the list.|
|||

Implementation examples:

```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.append(6)
>>> print(my_list)
[1, 2, 3, 4, 5, 6]

>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.extend([6, 7, 8])
>>> print(my_list)
[1, 2, 3, 4, 5, 6, 7, 8]

>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8]
>>> my_list.remove(6)
>>> print(my_list)
[1, 2, 3, 4, 5, 7, 8]


>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8]
>>> index_of_item = my_list.index(6)
>>> print(index_of_item)
5

>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.reverse()
>>> print(my_list)
[5, 4, 3, 2, 1]

>>> my_list = [1, 2, 3, 4, 5]
>>> copied_list = my_list.copy()
>>> print(copied_list)
[1, 2, 3, 4, 5]
```

Note: The copy() method creates a shallow copy of the list. So, if the list contains objects, the copy will refer to the same objects as the original list, and any modification made to the objects will be reflected in both the original and the copied list.

If you need a deep copy of the list, you can use the copy module in python, for example:

```python
import copy

original = [1, 2, [3, 4]]
deep_copied = copy.deepcopy(original)
```

Few more methods with more explanation:

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

`Pop()` method is used to remove an item from a list. It remove the item from the supplied index and returns the removed item. The default is to remove the last item (if no index is passed as argument).

```python
fruits = ['grape', 'banana', 'mango', 'orange']

# Remove the last item in the list (the string 'orange')
removed_item = fruits.pop()
print(fruits)

# Output: ['grape', 'banana', 'mango']
# and the variable removed_item contains the value 'orange'

# Remove the second item in the list (the string 'banana')
removed_item = fruits.pop(1)
print(fruits)
# Output: ['grape', 'mango']

# The variable removed_item contains the value 'banana'
```

The pop() method changes the list in-place. It modifies the original list and does not return a new list. But it returns the removed item, which can be used later if required.

### del

`del()` method remove an element from the list by index. For example:

```python
fruits = ['apple', 'banana', 'orange', 'grape']

# Use the del keyword to remove the third item in the list (the string 'orange')
del fruits[2]

print(fruits)
# Output: ['apple', 'banana', 'grape']
```

### remove()

The remove() method is used to remove an item from a list by value. It takes a value as an argument and removes the first occurrence of that value. It raises a ValueError if the item is not found in the list.

For example:

```python
fruits = ['apple', 'banana', 'orange', 'grape']

# Remove the string 'banana' from the list
fruits.remove('banana')

print(fruits)
# Output: ['apple', 'orange', 'grape']

# But it will raise value error if we do this:
fruits.remove('peas')

# Output: ValueError: list.remove(x): x not in list
```

Note: The remove() method only removes the first occurrence of the item, even if there are multiple occurrences of the item in the list. Here's an example:

```python
fruits = ['apple', 'grape', 'orange', 'grape', 'banana']

fruits.remove('grape')
print(fruits)
# Output: ['apple', 'orange', 'grape', 'banana']
```

So if we want to remove all occurrences, you need to use a loop.

### clear()

The clear() method is used to remove all items from a list. It is called on any list to remove all items from the list. For example:

```python
fruits = ['apple', 'banana', 'orange', 'grape']

# Remove all items from the list
fruits.clear()
print(fruits)

# Output: []
```

Note: The clear() method modifies the original list in-place. This means that after we call the clear() method, the list will be empty, and we cannot undo the operation. If you want to keep the original list unchanged, you can create a new list and copy the items from the original list into the new list, and then clear the original list. For example:

```python
fruits = ['apple', 'banana', 'orange', 'grape']

# Create a new list and copy the items from the original list
new_fruits = fruits[:]

# Clear the original list
fruits.clear()

# The original list is now empty, but the new_fruits list still contains the items.
```

## Flattening A Nested Lists

1. To flatten a nested list in Python, we can use the chain() method of the itertools module. The chain() method takes the elements of the nested list as an argument and returns a flattened version of the list, with all the sub-lists merged into a single list.

    For examples:

```python
from itertools import chain

# Define a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# chain the nested list
flattened_list = list(chain(*nested_list))
print(flattened_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Or we can use 'from_iterable method. It does not require list unpacking
merged = list(chain.from_iterable(nested_list))
print(merged)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

2. Using list comprehension:

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Their are other methods also available to flatten a list like concatenate method of numpy, extends method with loop, and sum(nested_list, []) etc.

## List-Unpacking

List unpacking allows us to assign the elements of a list to multiple variables in a single statement. It is a convenient way to extract the elements of a list and assign them to individual variables.

For example:

```python
# Define a list of numbers
numbers = [1, 2, 3]

# Unpack the elements of the list and assign them to separate variables
a, b, c = numbers
print(a, b, c)

# Output: 1 2 3

# Define a list of strings
fruits = ['apple', 'banana', 'orange']

# Unpack the elements of the list and assign them to separate variables
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3)
# Output: apple banana orange
```

This can make your code more concise and easier to read, especially when dealing with long lists or complex data structures.

Note: The number of variables used to unpack the elements of a list must match the number of elements in the list. If the number of variables doesn't match the number of elements, we will get a `ValueError` when we try to run the code.

For example:

```python
numbers = [1, 2, 3]

# Unpack the elements of the list and assign them to two variables, instead of three
a, b = numbers

# Output: ValueError: too many values to unpack (expected 2)
```

Here, the list contains three elements, but we are only trying to unpack the elements into two variables, so we get a ValueError. To avoid this error, make sure that the number of variables you use to unpack the elements of a list matches the number of elements in the list.

## List: All methods

```python
# Print a list of methods used to operate on lists.
# We will use the in-built dir() method for this task.
print([item for item in dir(list) if not item.startswith('_')])

['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

According to the Python docs, lists are used to store collection of **homogeneous items**, But a question may arise the list can contain any type of data like `items = ['one', 1, ['one', 'two'], (1, 2), {'one': 1}]`. So, why list is not heterogeneous instead of homogeneous?

The discussion about this can be: [read here](https://stackoverflow.com/questions/5150958/lists-in-python)

In brief, if we explore the discussion we find that The terms "semantic type" and "programmatic type" refer to different aspects of the data types used in programming languages.

The semantic type of a data type refers to the meaning or interpretation of the data that it represents. For example, a semantic type of "date" would indicate that the data represents a date and time value.

The programmatic type of a data type, on the other hand, refers to the specific implementation of the data type in a programming language. This includes things like the internal representation of the data, the operations that can be performed on it, and the specific syntax used to work with the data type in the language.

In short, the semantic type of a data type describes what the data represents, while the programmatic type describes how the data is implemented and used in a specific programming language.
