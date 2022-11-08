# Callable Objects in Python

Callable objects are functions like objects. We can use `callable()` built-in function to determine whether an object is callable.

Example:

```python
def double(a):
    return 2 * a


print(callable(double))
# Output: True
```

## Does a class also a callable in Python?
Lets check this:

```python

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)


print(callable(Person))
# Output: True
```

Let's check the methods and instances of this class. Are they also a callable?

```python

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)

# Check Instance
p = Person("John", "Doe")
print(callable(p))
# Output: False

# Check method of a class
print(callable(p.display))
# Output: True
```

So, the instance of a class is not callable but the methods of a class are callable.

## Can we make an instance a callable?
If a class defines a *__call__()* method, then its instances can also be callable.

Example:
```python
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __call__(self):
        return self.fname, self.lname

    def display(self):
        print(self.fname, self.lname)

p = Person("John", "Doe")
print(callable(p))
# Output: True
```

## The following are the callable objects in Python

- Built-in functions
- Built-in methods
- User-defined functions
- Methods
- Classes
- Class instance (On declaring __call__ method)
- Generators
- Coroutine functions



