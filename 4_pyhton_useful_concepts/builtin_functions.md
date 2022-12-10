abs()
aiter()
all()
any()
anext()
ascii()

bin()
bool()
breakpoint()
bytearray()
bytes()

callable()
chr()
classmethod()
compile()
complex()

delattr()
dict()
dir()
divmod()

enumerate()
eval()
exec()

filter()
float()
format()
frozenset()

getattr()
globals()

hasattr()
hash()
help()
hex()

id()
input()
int()
isinstance()
issubclass()
iter()

len()
list()
locals()

map()
max()
memoryview()
min()

next()

object()
oct()
open()
ord()

pow()
print()
property()

range()
repr()
reversed()
round()

set()
setattr()
slice()
sorted()
staticmethod()
str()

### sum()

The sum() function is used to calculate the sum of the elements of an iterable. It takes an iterable as an argument and returns the sum of the elements in the iterable.

For example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calculate the sum of the numbers in the list
result = sum(numbers)

print(result)

# Output: 45

# It also takes an optional argument called 'start', which specifies the value that the sum should start from.
# By default, the start argument is 0, so if you don't specify it, the sum() function will start the sum from 0.
result = sum(numbers, 10)
print(result)

# Output: 55
# It has started with 10, so 10 + 1 = 11, 11 + 2 = 13. So on...
```

super()

tuple()
type()

vars()

zip()

__import__()
