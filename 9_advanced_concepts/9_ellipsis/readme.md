# Ellipsis

Ellipsis or `...` is a singleton object. It is used as a placeholder in a function. We use the pyhon specific `pass` also for the same purpose.

## Python docs:
> The Ellipsis Object: 
This object is commonly used by slicing (see [Slicings](https://docs.python.org/3/reference/expressions.html#slicings)). It supports no special operations. There is exactly one ellipsis object, named Ellipsis (a built-in name). type(Ellipsis)() produces the Ellipsis singleton.

> It is written as Ellipsis or ....

## From typing module:
> Arbitrary-length homogeneous tuples can be expressed using one type and ellipsis, for example Tuple[int, ...]

> It is possible to declare the return type of a callable without specifying the call signature by substituting a literal ellipsis (three dots) for the list of arguments:

```python
def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    # Body

```

```python
def func():
    Ellipsis

def func():
    ...

print(func())
# Output: None
```

## Can be used as a default value for an argument

```python
def func(i = ...):
    return i

print(func())
# Output: Ellipsis

```

## Why Ellipsis is helpful?
```python
x=[]
x.append(x)
print(x)

# Output: Stringifying cyclical objects and returned [[...]]
```

```python
print([[...]])

# Output: Ellipses
```

## Slice notation
Ellipsis is an object that can appear in slice notation. 

```python
myList[1:2, ..., 0]
```

Ellipsis is also used in the Python standard library `typing module`.

Callable[..., int] to indicate a callable that returns an int without specifying the signature, or tuple[str, ...] to indicate a variable-length homogeneous tuple of strings. 