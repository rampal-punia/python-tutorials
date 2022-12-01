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
The name **dunder** derived from double underscore. In Python the Special methods are covered with double underscore. like `__str__`, `__dict__`, `__add__`, `__init__`.

Use python inbuilt method `dir()` to find out the list of all the double underscore methods for any python object.
```python
a_list = [1, 2, 3]
print(dir(a_list))

# Output:
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
    '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Upto __subclasshook__ are the double underscore methods.

# Further in tutorials we will understand how to extract the exact desired things from a list, like:
only_dunder = [item for item in dir(a_list) if item.startswith("__")]
print(only_dunder)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__']
```

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

## 7. Code blocks:
Many other languages uses `{}` to denote a code block. But, Python only uses `indentation` to denote a code block.

In the function below:
```python
def increment_by_5(number):
    number = number + 5
    return number

print(increment_by_5(4))
```
The second and third lines of code are indented by `4 spaces` to denote that it belong to the function `increment_by_5`. whereas the `print` statement is not indented, which denotes it is outside of the function.

Through out the tutorial, we will have plenty of examples to get used to it. 

print(increment_by_5(4))

## 8. PEP 8 – Style Guide for Python Code
From [Python docs](https://peps.python.org/pep-0001/):
> PEPs (Python Enhancement Proposals) are a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

PEP 8 gives coding conventions for the Python code comprising the standard library in the main Python distribution.
[Read more](https://peps.python.org/pep-0008/)


