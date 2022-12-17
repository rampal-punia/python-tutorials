# Functions

Block of codes designed to do one specific job, and can be called whenever required.

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
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."


greet = greeting("John", 12)
print(greet)

# Output: Hello John, you are 12 years old.
```

In the example above, we can not interchange the arguments, as the output would be a complete mess. For example:

```python
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."


greet = greeting(12, "John")
print(greet)

# Output: Hello 12, you are John years old

# It does not make sense, right!
# # Therefore the order of the positional arguments matters 
```

### Keywords Arguments

The keyword arguments are specified as name-value pair, rather than by its position in the function definition.

For example:

```python
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."


greet = greeting(name="John", age=12)
print(greet)

# Output: Hello John, you are 12 years old.
```

When we call the greeting function with the keyword arguments name='John' and age=12, the values of the keyword arguments are 'John' and 12, respectively. The order in which the arguments are specified in the function call does not matter, because the arguments are identified by their names.

Here the order of the arguments does not matters as the arguments are passed with their names. For example:

```python
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."


greet = greeting(age=12, name="John")
print(greet)

# Output: Hello John, you are 12 years old.
```

They can be used in conjunction with positional arguments, which are arguments specified by their position in the function definition.

### Default Values

## Returning data

### Simple data

### multiple values or values in a data structure
