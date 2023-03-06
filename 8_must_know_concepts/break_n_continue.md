# Break and Continue statements

The `break` and `continue` statements are the control flow statements in Python that are used to alter the normal flow of execution in a loop.

- Used in loops
- Used to alter the flow of a normal loop.
- These statements are useful in controlling our loops.

## Break

The `break` statement is used to break the flow of the loop. It helps the program to come out of the loop on meeting a specific condition. If it is used in the nested loops then it break the flow of the inner loop only.

### Example 1

- from the texts "A quick brown fox jumps over the lazy dog" print up to 's'

```python
string = "A quick brown fox jumps over the lazy dog"

for letter in string:
    if letter == 's':
        break
    print(letter)

print("Loop is terminated")
```

### Example 2

- from a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9] print every number up to '5'.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 5:
        break
    print(num)

print("Loop is terminated")
```

## Continue

The `continues` statement is used to continue the loop without iterating over the remaining statements inside the loop. This means, when the python interpreter sees the continue statement it gets back to the first line of the loop, so the rest of the code doesn't run in that iteration.

### Example-1

- from the texts "A quick brown fox jumps over the lazy dog" print everything except the letter 's'.

```python
string = "A quick brown fox jumps over the lazy dog"

for letter in string:
    if letter == 's':
        continue
    print(letter)

print("Loop is terminated")
```

### Example-2

- from a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9] print every number except 5.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 5:
        continue
    print(number)

print("Loop is terminated")
```

Note: The `break` statement will only exit the innermost loop in which it is used. If we have nested loops and we want to exit both loops, in this case, we can use the `break` statement in the inner loop and a `continue` statement in the outer loop to skip the rest of the outer loop's current iteration.
