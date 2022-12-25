# Sort() VS Sorted()

In Python, the `sort()` method and the `sorted()` function are both used to sort a sequence or collection of objects. However, they work in slightly different ways.

The sort() method is a method of the list class, and it is used to sort the elements of a list in place, meaning that it modifies the original list and does not return a new sorted list. It has the following syntax:

Copy code
list.sort(key=None, reverse=False)
The key argument is

|sort()|Sorted()|
|----------------------|------------------------|
|`sort` is a method only for the list class.| `sorted` is a function. It takes iterables like str, list, tuple and dictionary|
|sort is an in-place operation (i.e. it modifies the original list and does not return a new sorted list.)|sorted is not in -place hence time taken by it is more than sort.|
|sort returns none.| sorted returns a list which can be captured in a variable and used as-and-when required.|
|||

## sort()

### Syntax

```python
list.sort(key=None, reverse=False)

```

Example:

```python
l = [31, 24, 73, 88, 12]
print(l)

l.sort()
print(l)
```

## sorted()

### Syntax for sorted

```python
sorted(iterable, key=None, reverse=False)
```

```python
l = [31, 24, 73, 88, 12]
l1 = sorted(l)
print(l)
print(l1)

# Output:
[31, 24, 73, 88, 12]
[12, 24, 31, 73, 88]
```

In brief, `sorted()` function does not modify the original list, it returns a new sorted list, while the `sort()` method modifies the original list and returns `None`.
