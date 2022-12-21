# Lambda functions

A lambda function is a single line, small, and anonymous function. It can have multiple arguments, but it can only have a single expression.

## Syntax

```python
lambda parameters : expression
```

First, let's create a general Python to multiply two numbers.

```python
def multiply(a, b):
    result = a * b
    return result


result = multiply(3, 4)
print(result)

# Output: 12
```

Now let's convert the above function into a lambda function.

```python
# From the above definition, we know that lambda functions are 
# single line, small, and anonymous function, therefore

# First: make the above function single line
def multiply(a, b): return a * b        # this will still work and give the same results.
```

```python
# Second, make it small, by removing 'def' and 'return' keywords.
multiply(a, b): a * b                   # Of course, this will not work now
```

```python
# Third make it anonymous by taking away it's name, and place the word lambda there.
lambda a, b: a * b                      # Now, it will start working again

# This is an example of a lambda function that takes 2 arguments and returns
# the result of their multiplication.
```

```python
# Passing variables to a lambda function.
result = (lambda a, b: a * b)(3, 4)
print(result)
```

Lambda functions are often used as arguments to the Python's higher-order functions. Higher order functions are the functions that take in other functions as arguments.

## Using `filter function` with lambda

Suppose we want to filter the characters in a word where the Unicode code value of the character is more than '110'. We will use `filter()` function here, and pass the lambda function as a first argument and the word(any iterable, in this case string) to the filter function.

```python
# Define a word
word = "Python"

# First let's check the Unicode code values of each character.
ord_values = [(letter, ord(letter)) for letter in word]
print(ord_values)   
# Output: [('P', 80), ('y', 121), ('t', 116), ('h', 104), ('o', 111), ('n', 110)]

# Use higher order function 'filter' to filter values > 110
print(list(filter(lambda x: ord(x) > 110, word)))
# Output: ['y', 't', 'o']
```

The filter function in Python takes in a function and a list as arguments, and returns a new list that contains only the elements from the original list for which the condition of the filter function returned True.

Let's check another example, where we filter the odd numbers only from a list of numbers using filter and `lambda function`.

```python
# Define a list
numbers = [458, 569, 1254, 3652, 562, 2541, 889, 568, 997, 542, 325]

# filter only the odd numbers
odd_num_list = list(filter(lambda x: x % 2 == 1, numbers))

print(odd_num_list)
# Output: [569, 2541, 889, 997, 325]
```

## Using `map function` with lambda

Suppose we need to convert each number of a list into its square. We will use another higher order function `map()` for this task.

```python
# Define a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using 'map function' to map each element of the list to its power using lambda function.
print(list(map(lambda num: pow(num, 2), numbers)))
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Advantages and disadvantages of Lambda functions

### Advantages

- Smaller syntax
- Can be passed easily as an argument
- Can take any number of arguments

### Disadvantages

- Can not be called multiple times
- Hard to debug and error handling
- One and only one expression
