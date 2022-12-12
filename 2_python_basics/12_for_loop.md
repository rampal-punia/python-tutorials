# For Loop In Python

The for loop is used to iterate over a sequence of items, such as a list, str, tuple. The for loop will iterate over each item in the sequence, and it will execute the code in the loop block for each item.

The Python documentation:

>The for statement in Python differs a bit from what you may be used to in other programming languages. Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

```python
animals = ['cat', 'elephant', 'tiger']
for w in animals:
    print(w, len(w))

# Output:
cat 3
elephant 8
tiger 5
```

## For loop: Strings

```python
word = 'abracadabra'
for letter in word:
    print(letter)

```

## For loop: Lists

```python
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Use the for loop to iterate over the list
for number in numbers:
    # This code will be executed for each item in the list
    print(number)
```

## For loop: Dictionaries

We can use the for loop to iterate over the keys, values, or items in a dictionary. For example, using a for loop to iterate over the keys in a dictionary:

```python
# Define a dictionary
my_dict = {"name": "John", "age": 25, "gender": "Male"}

# Use the for loop to iterate over the keys in the dictionary
for key in my_dict:
    # This code will be executed for each key in the dictionary
    print(key)


# Output: 
name
age
gender
```

Using the values() method to iterate over the values in a dictionary, like this:

```python
# Define a dictionary
my_dict = {"name": "John", "age": 25, "gender": "Male"}

# Use the for loop to iterate over the values in the dictionary
for value in my_dict.values():
    # This code will be executed for each value in the dictionary
    print(value)

# Output:
John
25
Male
```

Finally, we can use the items() method to iterate over the items in a dictionary, which are represented as key-value pairs. For example:

```python
# Define a dictionary
my_dict = {"name": "John", "age": 25, "gender": "Male"}

# Use the for loop to iterate over the items in the dictionary
for value in my_dict.items():
    # This code will be executed for each item in the dictionary
    print(value)

# Output:
('name', 'John')
('age', 25)
('gender', 'Male')
```

## range()

We can also use the `range()` function to define a range of numbers to iterate over. For example:

```python
# Use the range() function to define a range of numbers
for number in range(1, 11):
    # This code will be executed for each number in the range
    print(number)
```

Iterating over a reversed list:

```python
for i in reversed(range(1, 10, 2)):
    print(i, end=' ')

# Output:
9 7 5 3 1
```

Iterating on a list after sorting the elements:

```python
basket = ['orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(basket):
    print(fruit.capitalize())

# Output:
Apple
Banana
Orange
Orange
Pear
```

To loop over two or more sequences at the same time, the entries can be paired with the zip() function. For example:

```python
questions = ['name', 'school', 'roll number']
answers = ['John', 'ABC School', 20]
for que, ans in zip(questions, answers):
    print(f'What is your {que}?')
    print(f'It is {ans}.')

# Output:
What is your name?
It is John.
What is your school?
It is ABC School.
What is your roll number?
It is 20.
```

## Enumerate()

The enumerate() method is used to iterate over a sequence of items and retrieve the index and value of each item. This is useful when we require both the index and the value of each item in a list or other sequence.

Here is an example of using the enumerate() method in a for loop:

```python
# Define a list of numbers
letters = ['a', 'b', 'c', 'd', 'e']

# Use the enumerate() method to iterate over the list.
# The enumerate object yields pairs containing a count (from start, which defaults to zero) 
# and a value yielded by the iterable argument.
for index, value in enumerate(letters):
    # This code will be executed for each item in the list
    print(f"Index: {index}, Value: {value}")

# Output:
Index: 0, Value: a
Index: 1, Value: b
Index: 2, Value: c
Index: 3, Value: d
Index: 4, Value: e
```

We can also specify a start index for the enumerate() method by passing it as an argument. Enumerate takes an optional argument `start`, to start index from. For example:

```python
# Define a word
word = "Python"

# Use the enumerate() method to iterate over each letter of the word, and start indexing from 11.
for index, value in enumerate(word, 11):
    # This code will be executed for each item in the list
    print(f"Index: {index}, Value: {value}")

# Output:
Index: 11, Value: P
Index: 12, Value: y
Index: 13, Value: t
Index: 14, Value: h
Index: 15, Value: o
Index: 16, Value: n
```

## for-else

In Python, the `else` keyword can be used in combination with a `for` loop to specify a block of code that should be executed when the loop completes successfully.

```python
# Define a letter.
guess = 'k'

# Define a list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Use the for loop to iterate over the list
for letter in letters:
    # This code will be executed for each item in the list
    if letter == guess:
        print(f"Found guessed letter '{guess}' in the list.")
        # Use the break statement to exit the loop
        break
else:
    # This code will only be executed if the loop completes successfully, without break.
    print(f"The guessed letter '{guess}' is not found!")

# Output(guess = 'k'): The guessed letter 'k' is not found!
# Output(guess = 'e'): Found guessed letter 'e' in the list.
```
