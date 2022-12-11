# Comparison Operators

Comparison operators are used to compare two values and determine their relationship. The result of a comparison operator is either `True or False`.

Here are the comparison operators in Python:

|Operator|Explanation|Example|
|-----------------------|-----------------------------|-----------------------------|
|`==`|Check if two values are equal | `7 == 7` returns True, while `7 == 9` returns False|
|`!=`|Check if two values are not equal|`7 != 7` returns False, while `7 != 9` returns True|
|`>` |Check if the value on the left is greater than the value on the right| `7 > 9` returns False, while`9 > 7` returns True|
|`<` |Check if the value on the left is less than the value on the right|`7 < 9` returns True, while `9 < 7` returns False|
|`>=`|Check if the value on the left is greater than or equal to the value on the right|`7 >= 9` returns False, while `9 >= 7` returns True|
|`<=`|Check if the value on the left is less than or equal to the value on the right|`7 <= 9` returns True, while `9 <= 7` returns False|

These operators can be used in `if statements` to control the flow of a program based on the result of a comparison.

For example:

```python
# Define two variables
x = 9
y = 7

# Use the comparison operator to check if x is greater than y
if x > y:
    print("x is greater than y")
else:
    print("x is less than y")

# Output: x is greater than y
```

In this code, the if statement uses the > operator to check if the value of x is greater than the value of y. Since it is, it prints the message "x is greater than y".
