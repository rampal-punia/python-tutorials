# Sort() VS Sorted()

|sort()|Sorted()|
|----------------------|------------------------|
|`sort` is a method only for the list.| `sorted` is a function. it takes iterables like str, list, tuple and dictionary|
|sort returns none.| sorted returns a list which can be captured in a variable and used as-and-when required.||
|sort is an in-place operation (i.e. the original list itself is modified)|Sorted is not in -place hence time taken by it is more than sort|
|||

## sort()

```python
l = [31, 24, 73, 88, 12]
print(l)

l.sort()
print(l)
```

## sorted()

```python
l = [31, 24, 73, 88, 12]
l1 = sorted(l)
print(l)
print(l1)

# Output:
[31, 24, 73, 88, 12]
[12, 24, 31, 73, 88]
```
