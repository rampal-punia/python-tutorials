# Modules

Creating modules is a way to keep code blocks (classes and function definitions) in a file to use them in another scripts. The definitions from a module can be imported into other modules. So we can say, a module is a file containing Python definitions and statements.

Modules can be used to organize and reuse code, making it easier to develop and maintain large programs. For example, you might create a module that contains functions for performing mathematical operations, and then import that module into different programs that need to perform those operations. The module's name (as a string) is available as the value of the global variable `__name__` within a module.

The file extension is the module name with the suffix `.py`. For example create a file named `color_generator.py` with the following code:

```python
import random

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_color_hex():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'
```

Create another py file with name `main.py` or enter the Python interpreter and import this module with the following command:

```python
import color_generator
```

This does not add the names of the functions defined in `color_generator.py` directly to the current namespace for direct use; it only adds the module name `color_generator` there. Now using the module name we can access the functions like this:

```python
import color_generator

color = color_generator.random_color()
print(color)

# output: (186, 91, 231)
```

or to use the another function `random_color_hex` we can do:

```python
import color_generator

color = color_generator.random_color_hex()
print(color)

# output: #b6ed31
```

If we need to use a function from a module very often, we can assign it to a local name:

```python
clr = color_generator.random_color
```

Also we can import a module with some alias names like:

```python
import color_generator as clr_gn

color = clr_gn.random_color()
print(color)
```

or, we can directly import the function name using `from` keyword, like:

```python
from color_generator import random_color_hex as clr_hx

color = clr_hx()
print(color)

# output: #1ccf42
```
