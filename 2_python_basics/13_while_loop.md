# While Loop

A while loop in Python will continue to execute a block of code as long as a certain condition is met(True). It will first evaluate the condition, and if it is true, it will execute the code block.

After the code block has been executed, the while loop will go back to the condition and re-evaluate it. If the condition is still true, the code block will be executed again, and this process will repeat until the condition becomes false.

If we pass a condition that is always true then the while loop will run for ever!

Syntax:

```python
# define the loop condition
while condition:
    # code to be executed in the loop

```

When the condition becomes false, the loop will terminate. The program will continue to execute any code that comes after the while loop.

Example:

```python
# initialize a variable
i = 0

# define the loop condition
while i < 10:
    # Current iteration number
    print(i)
    
    # update the variable 'i'.
    i = i + 1
```

The loop will continue to run as long as the value of `i` is less than 10. The loop will terminate once `i` becomes equal to 10.

## Simple number guessing game using While loop

```python
selected_number = 11
user_guess = 0

while user_guess != selected_number:
    user_guess = int(input("Guess a number: "))

print("Correct!")
```
