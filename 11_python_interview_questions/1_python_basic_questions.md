# Python questions (Python Basics)

## Questions

- What are the characteristics of Python Language?
- Difference between Interpreted and Compiled languages.
- Name the built-in data types in Python.
- What are the practical use cases of Python Language?
- What is PEP-8?
- How do we write programs in Python?
- Define "block of codes" in Python.
- What are the .py and .pyc files?
- Can we change the id, and type of an object in Python?
- What are the keywords in Python?

## 1. What are the characteristics of Python Programming Language?

Ans: Python is

- Easy to learn
- Powerful & interpreted programming language
- Efficient high-level data structures
- Effective approach to object-oriented programming
- Elegant syntax and dynamic typing
- Ideal for scripting and rapid application development
- Useful in various domains on most platforms

## 2. Difference between Interpreted and Compiled languages

Ans: Codes written in high-level languages are required to be translated into machine codes or binary codes with the help of interpreters or compilers.

### Compiled languages

The complete source code is compiled into binary code by a compiler. It is not completely portable and can not run on every platform. Once compiled the source code can be run again and again as required.
C, C++, Rust and Go are a few examples of compiled languages.

### Interpreted Languages

Instead of complete source code, the interpreter translates the source code instructions by instructions into binary code. Therefore when each time we run a program an interpreter runs.
Python, Ruby, PHP and JavaScript are a few examples of compiled languages.

## 3. Name the built-in data types in Python

Ans: The built-n data types in Python are:

- String
- Numeric
  - Integer
    - Booleans are a subtype of integers
  - Float
  - Complex Numbers
- Sequence Type
  - List
  - Tuple
  - Range
- Mapping Type
  - Dictionary
- Set types
  - Set
  - Frozenset
- Binary Sequence Type
  - Bytes
  - Bytearray
  - Memoryview

## 4. What are the practical use cases of Python Language?

Ans: Python is used for:

⚡ Software Development
⚡ Web Development
⚡ Games Automation
⚡ Desktop GUI Development
⚡ Tasks automation
⚡ Data Analysis and Visualization
⚡ Predictive Analysis
⚡ Statistics
⚡ Data Science
⚡ Organizing Finances
⚡ Machine Learning / Artificial Intelligence / Deep Learning
⚡ Audio and Video Applications

## 5. What is PEP-8

Ans: PEPs (Python Enhancement Proposals)
PEPs are design documents providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

PEP 8 gives coding conventions for the Python code comprising the standard library in the main Python distribution.

## 6. How do we write programs in Python?

Ans: The most common ways to write a Python program are:

Interactive Mode:

Open the Python interpreter by running the python command in the terminal or command prompt and then write Python code directly in the interpreter. This method is good for learning.

Script Mode:

Create a plain text file with the .py extension and write the Python code in this file using any text editor. Once the code is completed run it by typing python <filename>.py in the terminal or command prompt.

IDE (Integrated Development Environment) Mode:

An IDE is a software application that provides a comprehensive environment for writing, testing, and debugging code.  To build software we generally work inside an IDE.

## 7. Define "block of codes" in Python

Ans: In Python

A block of code refers to a group of statements that are executed together.

Blocks of code are defined by indentation. In Python, indentation is used to indicate the level of nested code and to indicate which statements belong to a specific block...

```python
def my_function():
    statement_1
    statement_2
    statement_3
```

## 8. What are the .py and .pyc files?

`.py` files are the source code files containing Python code. These files are executed by the Python interpreter. When we run a .py file, the Python interpreter reads the code, compiles it, and then runs the resulting bytecode.

`.pyc` files are the compiled version of the .py files. They are created by the Python interpreter when a .py file is imported or run. The Python interpreter uses the compiled bytecode in the .pyc file to improve the performance of the program by avoiding the need for recompiling the source code every time the program runs. The .pyc files are created in the pycache directory, which is located in the same directory as the original .py file.

Also, the .pyc files can be deleted without affecting the program as the interpreter will create them again whenever required...

## 9. can we change the id, and type of an object in Python?

Ans: In Python, the id() function returns a unique integer that represents the memory location of an object. The type() function returns the type of an object.

We can not change the id and the type of a python object once it is created.

From Python doc:
"An object’s type determines the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type. The type() function returns an object’s type (which is an object itself). Like its identity, an object’s type is also unchangeable."

We use the type() function can get another copy of the object. For example, we can use the int(), str(), float() and other functions to convert an object from one type to another...

## 10. What are the keywords in Python?

Ans: Keywords are reserved words that have a special meaning and cannot be used as variable names or function names.

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
