# Logical Operators

The logical operators are used to combine multiple conditions in an if statement. The result of a logical operator is either True or False.

Here are the logical operators in Python:

|Operator|Explanation|Example|
|-----------|----------------------|-----------------------------|
|`and` | Combine two conditions, and the resulting condition is True only if both conditions are True| `3 > 2 and 5 > 3` returns True, while `3 > 5 and 5 > 3` returns False|
|`or` | Combine two conditions, and the resulting condition is True if either of the conditions is True| `3 > 5 or 5 > 3` returns True, while `3 > 5 or 5 > 6` returns False|
|`not` |Negate a condition, so that True becomes False and False becomes True| `not 3 > 5` returns True, while `not 5 > 3 returns` False|

These operators can be used in if statements to control the flow of a program based on multiple conditions.

## 'And' operator

Combine two conditions, and the resulting condition is True only if both conditions are True

For example:

```python
# Define age variables
age = 25

# Use the logical operator to check if age is greater than 18 and less than 60
if age > 18 and age < 60:
    print("Eligible")
else:
    print("Not Eligible")

# Output: Eligible
```

In Python we can write the above code just like we write it in mathematics. For example:

```python
# Define age variables
age = 25

if 18 <age < 60:        # Just like mathematics expression
    print("Eligible")
else:
    print("Not Eligible")

# Output: Eligible
```

For more than one variable:

```python
age = 30
language = 'PHP'
languages = ['Python', 'JavaScript', 'Ruby']

# Use the logical operator to check if x is greater than 2 and y is less than 4
if age > 25 and language in languages:
    print("Eligible")
else:
    print("Not Eligible")

```

## Or operator

Combine two conditions, and the resulting condition is True if either of the conditions is True

```python
# Define variables
age = 30
language = 'PHP'
languages = ['Python', 'JavaScript', 'Ruby']

# Use the logical operator to check if x is greater than 2 and y is less than 4
if age > 25 or language in languages:
    print("Eligible")
else:
    print("Not Eligible")
```

## Not operator

Negate a condition, so that True becomes False and False becomes True

```python
# Define two variables
age = 25

# Use the logical operator to check if x is greater than 2 and y is less than 4
if not 18 < age < 60:
    print("Not Eligible")
else:
    print("Eligible")

# Output: Eligible
```
