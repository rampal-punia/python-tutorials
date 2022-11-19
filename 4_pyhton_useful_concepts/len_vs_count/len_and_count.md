# Coding Mantras

## Python Tutorial: Using Len function

<br>

## About len
    • It is a function, not a method.
    • It returns an 'int'.
    • It takes a container as an input.
    • Return the number of items in that container.
    • when we use len(object) python internally calls the __len__ method.

## Syntax
```python
len(iterable)
```

## Len function with *strings*
```python
an_str = "Hello world"
print(len(an_str))
```

<br>


## Len function with *tuple*
```python
a_tuple = (0, 1, 2, 3, 4, 5, 6, 7)
print(len(a_tuple))
```

<br>


## Len function with *list*
```python
a_list = ['a', 'd', 'k', 'm', 'o']
print(len(a_list))
```

<br>


## Len function with *dictionary*
```python
a_dict = {"id": 21123, "name": "John", "age": 21}
print(len(a_dict))
```

<br>


## Len function with *set*
```python
a_set = {3, 45, 75, 34, 44}
print(len(a_set))
```

<br>


## Python Tutorial: Using count method

<br>

## About count
    • It is a method, not a function.
    • In strings: It returns the number of non-overlapping  occurrences of substring sub in string S[start: end].
    • In list and tuple: Returns the number of occurrences of a value.
    • It returns an 'int'.

## Syntax
```python
str.count('a_sub_string_here')
tuple.count(an_element_here)
list.count(an_element_here)
```

## Count method with *strings*
```python
an_str = "Hello world"
print(an_str.count("o"))
print(an_str.count("wo"))
```

<br>


## Count method with *tuple*
```python
a_tuple = (3, 1, 7, 3, 4, 5, 3, 7)
print(a_tuple.count(3))
```

<br>


## Count method with *list*
```python
a_list = ['a', 'd', 'a', 'k', 'm', 'a', 'o']
print(a_list.count('a'))
```


# Thanks For Watching. Like, share & Subscribe Coding Mantras.