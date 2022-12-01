# Styles and Conventions

Python is an interpreted language. It has it's set of rules and grammar, just like any other language.

Let's check them one by one.

## 1. Comments
A single line comment starts with `#`.
```python
# This is a comment

a = b + 5   # This is an inline comment. 
```

For documenting a Python function, class or module use triple quotes. `""" """`
```python
def add(a, b):
    """A function to add two variables.

    Args:
    a = int
    b = int 
    
    Return:
    Result(int) of sum of two integers.
    """

    return a + b
```

## 2. Variables naming
- Start with a letter or the underscore character
- Cannot start with a number
- Contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Case-sensitive (name, Name, NAME are different)

## 3. Functions and Classes naming
Function names follow the same convention as variable names.

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

```python
def calculate_area(radius):
    ...
```

## 4. Code continuation in next line
Using `\` to denote the code continuation to the next line.
```python
result = first_number + \
        second_number + \
        third_number

# But in case of (), and [] '\' is not required.
result = (first_number +
          second_number +
          third_number)
# or
a_long_list = ['A', 'quick', 'brown', 'fox',
               'jumps', 'over', 'a', 'lazy', 'dog']
```

## 5. Dunder methods
The name **dunder** derived from double underscore. In Python the Special methods are covered with double underscore. like `__str__`, `__dict__`, `__add__`, `__init__`

## 6. Reserved keywords
The following words are [reserved keywords](https://docs.python.org/3.8/reference/lexical_analysis.html#keywords) in Python programming language:

||||||||
|-----|-----|-----|-----|-----|-----|-----|
|False|await|else |import|pass|None|break|
|except|in|raise|True|class|finally|is|
|return|and|continue|for|lambda|try|as|
|def|from|nonlocal|while|assert|del|global|
|not|with|async|elif|if|or|yield|
||||||||

## 7. PEP 8 – Style Guide for Python Code
From [Python docs](https://peps.python.org/pep-0001/):
> PEPs (Python Enhancement Proposals) are a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

PEP 8 gives coding conventions for the Python code comprising the standard library in the main Python distribution.
[Read more](https://peps.python.org/pep-0008/)


