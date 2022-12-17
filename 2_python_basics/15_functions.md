# Functions

Block of codes designed to do one specific job, and can be called whenever required.

The aim of declaring a function is to write a set of related codes together and execute it as a unit. Functions allow us to reuse code, make our code easier to read and maintain, and divide a large program into smaller, more manageable chunks.

## Declaring a Function

We use the keyword `def` for a function definition. It must be followed by the function name. We can pass the parameters inside the parenthesis () that follows the function name.

For example:

```python
def addition(num1, num2):
    return num1 + num2
```

The statements that form the body of the function start at the next line, and must be indented. The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. It is a good practice to include **docstrings** for a function code.

```python
def addition(num1, num2):
    """A function to add two numbers.

    Args:
        num1 (int): any number
        num2 (int): any number

    Returns:
        int: sum of the two numbers
    """
    return num1 + num2
```

## Pass data to a function and call the call the function

```python
def addition(num1, num2):
    return num1 + num2

result = addition(3, 5)
print(result)
```

## Parameter Vs Argument

**Parameters**: Variables used inside the function definitions. In other words parameters are declared with the function
declaration as a placeholders for the values they work upon.

How to remember:
**Parameters: Placeholders (P-P)**

**Arguments**: The values/data passed against the function parameters. The arguments are the actual values for the placeholders
in a function.

How to remember:
**Arguments: Actual values (A-A)**

```python
# Parameters: a, b, c(Placeholders)
def multiply(a, b, c):
    return a * b * c

# Arguments: 4, 5, 6(Actual values)
result = multiply(4, 5, 6)
print(result)
```

In short, parameters are variables that are defined in the function definition, and arguments are the values passed to the function when it is called.

## Arguments can be passed to a function in various ways

### Positional Arguments

Positional arguments are arguments that are passed to a function in a specific order defined while declaring a function. It means, while calling a function with positional arguments, the order in which the arguments are passed to the function must match the order of the parameters in the function definition.

Positional arguments are typically used when the order of the arguments is important. We can not change the order of the positional arguments in may cases the result may vary, or a syntax error may occur.

For example:

```python
def greeting(name, language):
    return f"Hello {name}, you favorite language is {language}."


greet = greeting("John", "Python")
print(greet)

# Output: Hello John, you favorite language is Python.
```

In the example above, we can not interchange the arguments, as the output would be a complete mess. For example:

```python
def greeting(name, language):
    return f"Hello {name}, you favorite language is {language}."


greet = greeting("Python", "John")
print(greet)

# Output: Hello Python, you favorite language is John.

# It does not make sense, right!
# Therefore the order of the positional arguments matters!
```

### Keywords Arguments

The keyword arguments are specified as name-value pair, rather than by its position in the function definition.

For example:

```python
def greeting(name, language):
    return f"Hello {name}, you favorite language is {language}."


greet = greeting(name="John", language="Python")
print(greet)

# Output: Hello John, you favorite language is Python.
```

When we call the greeting function with the keyword arguments name='John' and age=12, the values of the keyword arguments are 'John' and 12, respectively. The order in which the arguments are specified in the function call does not matter, because the arguments are identified by their names.

Here the order of the arguments does not matters as the arguments are passed with their names. For example:

```python
def greeting(name, language):
    return f"Hello {name}, you favorite language is {language}."


greet = greeting(language="Python", name="John")
print(greet)

# Output: Hello John, you favorite language is Python.
```

They can be used in conjunction with positional arguments. For example:

```python
def greeting(name, language, experience):
    return f"Hello {name}, you favorite language is {language}. You have {experience} years of experience."


greet = greeting("John", "Python", experience=5)
print(greet)

# Output: Hello John, you favorite language is Python. You have 5 years of experience.
```

### Default Arguments

The default arguments take a default value if no value is provided for it during the function call. Default arguments are specified in the function definition, after the positional/non-default arguments.

For example:

```python
def greeting(name, language="Python"):
    return f"Hello {name}! Do you enjoy learning {language}."


greet = greeting("John")
print(greet)

# Output: Hello John! Do you enjoy learning Python.
```

## Returning data

The `return` keyword is used to return a value or expression from a function. For example:

```python
def divide(a, b):
    return a / b


result = divide(10, 4)
print(result)

# Output : 2.5
```

In the example above, the divide function takes two arguments, `a` and `b`, and divides a with b. The result is then returned to the caller using the `return` statement.

We can return multiple values from a function in a `tuple`. For example:

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    fraction_result = a/b
    return quotient, remainder, fraction_result


results = divide(11, 4)
print(results)

# Output: (2, 3, 2.75)
```
