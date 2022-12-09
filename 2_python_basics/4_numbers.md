# Numbers

Number representations in Python:

```python
x = 20          # int
print(x)
# Output: 20

x = 20.897      # float
print(x)
# Output: 20.897

x = 20 + 8j     # complex number
print(x)
# Output: (20+8j)
```

## Binary Representation

```python
x = 0b110100    # binary (accepts only 0 and 1 after 0b)
print(x)        # Output: 52

print(bin(x))   # Output: 0b110100
```

## Octal Representation

```python
x = 0o710    # Hexadecimal (accepts only 0-9, and a-f)
print(x)        # Output: 456

print(oct(x))   # Output: 0o710
```

## Hexadecimal Representation

```python
x = 0xef10    # Hexadecimal (accepts only 0-9, and a-f)
print(x)        # Output: 61200

print(hex(x))   # Output: 0xef10
```

**Recap**:

- `0b` for binary
- `0o` for octal
- `0x` for hexadecimal

## Arithmetic Operators

In a Python interpreter:

```python
>>> 3 + 2       # addition
5

>>> 3 - 2       # subtraction
1

>>> 3 * 2       # multiplication
6

>>> 3 / 2       # float division
1.5

# Even 2 divided by 2 returns float(1.0)
>>> 2 / 2
1.0

>>> 3 // 2      # floor division (discards the fractional part)
1

>>> 3 * 2 / 2 + 2   # mathematical expression calculation
5.0

>>> 3 ** 2      # `**` denotes power by the following number
9

>>> 3 ** 3      # 3 raised to the power of 3
27

# modulus of the number
>>> 3 % 2       # remainder of the 3 divided by 2       
1

>>> 10 % 4      # remainder of the 10 divided by 4       
2
```

## Useful math functions

```python

# abs()
x = -20.155
print(abs(x))
# Output: 20.155

# --------------------------------------------------------------- #
# int()
x = "20"            # x is string here
print(id(x))        # 140168494222512
print(type(x))      # <class 'str'>

x = int(x)          # converting to int(check note below)
print(id(x))        # 9801856
print(type(x))      # <class 'int'>

# note: Initially 'string 20' was assigned to x. The type function has not changed the type of that string 20. But created another int object 20 at some different location and assigned that 20 to the variable x. The string object is immutable in Python(more on this discussed later), it can not be changed. You can check the id() This is the reason both of both the x are different.

# --------------------------------------------------------------- #
# round()
>>> round(4.402)    # round a number to the nearest decimal point
4

>>> round(4.602)   
5

# first argument, second argument up to which the given number to be rounded.
>>> round(4.0987654, 3)  
4.099
```

## Augmented Assignment Operators

```python
x = 20
# Same as (x = x + 2)
x += 2
print(x)
# Output: 22

x = 20
# Same as (x = x - 2)
x -= 2
print(x)
# Output: 18

# Similarly we can use
x *=2       # Output: 40

x/2= 2      # Output: 10.0

x %= 2      # Output: 0

x **= 2     # # Output: 400
```

## Int: All methods

Using `dir()` method to list all the methods of int.

```python
print([item for item in dir(y) if not item.startswith('_')])

# Output:
['as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

Let's see all the methods one by one:

```python
x = 56000/100
print(x.as_integer_ratio())

# Output: (560, 1)
#--------------------------#

y = 56
print(y.denominator)
# Output: 1
print(y.numerator)
# Output: 56
print(y.bit_length())
# Output: 6


z = 56 + 5j
a = 7
b = b'\x07\x00'
print(z.conjugate())
print(z.imag)


print(a.to_bytes(2, 'little'))
print(int.from_bytes(b, 'little'))

```
