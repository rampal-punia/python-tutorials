# Difference between len() and count()

In python, both the `len()` function and the `count()` method are built-in functions that are used to retrieve information about a sequence or collection of objects.

|len()|count()|
|-------------|---------------------|
|It is a function, not a method. <br> It returns the length of a sequence. It can be used on any object that supports the len() function, including strings, lists, tuples, and dictionaries.<br>It takes a container as an input.<br>Return the number of items in that container.<br>when we use len(object) python internally calls the `__len__` method.|It is a method, not a function.<br> it returns an integer indicating the number of times the specified element appears in the sequence. <br>It is used to count the number of occurrences of a specific element in a sequence or collection. <br> In strings: It returns the number of non-overlapping occurrences of substring sub in string S[start: end]. Optional arguments start and end are interpreted as in slice notation.<br>In list and tuple: It returns the number of occurrences of a value. It cannot be used on dictionaries or other unordered collections.<br>|
|||

## len(): Syntax

```python
len(iterable)
```

## len(): with *strings*

```python
an_str = "Hello world"
print(len(an_str))
```

## len(): with *tuple*

```python
a_tuple = (0, 1, 2, 3, 4, 5, 6, 7)
print(len(a_tuple))
```

## len(): with *list*

```python
a_list = ['a', 'd', 'k', 'm', 'o']
print(len(a_list))
```

## len(): with *dictionary*

```python
a_dict = {"id": 21123, "name": "John", "age": 21}
print(len(a_dict))
```

## len(): with *set*

```python
a_set = {3, 45, 75, 34, 44}
print(len(a_set))
```

## count(): Syntax

```python
str.count('a_sub_string_here')
tuple.count(an_element_here)
list.count(an_element_here)
```

## Count(): with *strings*

```python
an_str = "Hello world"
print(an_str.count("o"))
print(an_str.count("wo"))
```

## Count(): with *tuple*

```python
a_tuple = (3, 1, 7, 3, 4, 5, 3, 7)
print(a_tuple.count(3))
```

## Count(): with *list*

```python

a_list = ['a', 'd', 'a', 'k', 'm', 'a', 'o']
print(a_list.count('a'))
```
