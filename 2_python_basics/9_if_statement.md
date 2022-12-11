# If statement (Handling Conditions in Python)

The if statement in Python is used to control the flow of a program based on a condition. The if statement evaluates the condition, and if it is True, it executes the code in the following block. If the condition is False, it skips the code in the following block.

```python
# Define a variable
number = 5

# Use the if statement to check if x is greater than 3
if number > 0:
    # This code will only run if the condition (number > 3) is True
    print("Number is positive")

# Output: Number is positive
```

## If - else block

We can also use the `else` keyword to specify a block of code that should be executed if the condition is False.

For example:

```python
# Define a variable
number = -5

# Use the if statement to check if x is greater than 3
if number > 0:
    # This code will only run if the condition (number > 3) is True
    print("Number is positive")

else:
    # This code will only run if the condition (number > 3) is False
    print("Number is either zero(0) or negative")

# output: print("Number is either zero(0) or negative")
```

## If - elif - else block

We can also use the `elif` keyword to specify additional conditions that should be checked if the original condition is False. There can be multiple `elif` conditions.

For example:

```python
# Define a variable
number = -5

# Use the if statement to check if x is greater than 3
if number > 0:
    # This code will only run if the condition (number > 3) is True
    print("It is a positive number.")

elif number == 0:
    # This code will only run if the condition (number > 3) is False
    print("It is a zero(0).")
else:
    # This code will only run if the condition (number > 3) is False
    print("It is a negative number.")

# Output: It is a negative number.

# And if we do:
number = 0

# Use the if statement to check if x is greater than 3
if number > 0:
    # This code will only run if the condition (number > 3) is True
    print("It is a positive number.")

elif number == 0:
    # This code will only run if the condition (number > 3) is False
    print("It is a zero(0).")
else:
    # This code will only run if the condition (number > 3) is False
    print("It is a negative number.")

# Output: It is a zero(0)
```

## Ternary conditional operators

Using a conditional operation in a single line as a switch to get one or another value. Ternary specifically means having three inputs.

Syntax: [on_condition_true] if [condition] else [on_condition_false]

## using help function of Python to get help

```python
print(help('if'))

# Output:
The "if" statement
******************

The "if" statement is used for conditional execution:

   if_stmt ::= "if" assignment_expression ":" suite
               ("elif" assignment_expression ":" suite)*
               ["else" ":" suite]

It selects exactly one of the suites by evaluating the expressions one
by one until one is found to be true (see section Boolean operations
for the definition of true and false); then that suite is executed
(and no other part of the "if" statement is executed or evaluated).
If all expressions are false, the suite of the "else" clause, if
present, is executed.

Related help topics: TRUTHVALUE
```
