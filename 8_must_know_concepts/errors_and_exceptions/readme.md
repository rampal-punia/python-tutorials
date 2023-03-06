# Exception Handling In Python

Python exception handling in easiest way with code snippets.

try:
    read_this_thread()
except Exception as ex:
    i_already_knew_this()
else:
    now_i_know_it_well()
finally:
    scroll_away()

---
What is an exception?

An exception is a Python object that represents an error.

It is an event, which occurs during the execution of a program where a Python script encounters a situation that it cannot handle, it raises an exception.

For example:

```python
num = 'A string' + 5

print(num)
```

To prevents the program from getting crashed, we use exception handling using try-except blocks.

The code that might raise an exception is placed in a "try" block, and the code to handle the exception is placed in an "except" block.

For example

Let's add try-except block to our code and handle the error thrown by the above program.

```python
try:
    num = 'A string' + 5
except Exception as ex:
    print(f'[ERROR CODE 111]\n{ex}')
    num = 2 + 5
print(num)
```

Note: Giving an error code is the developer's specific for logging the error and then figuring out exactly inside the code-base that raised it.

Using multiple except statements to catch the different exceptions.

```python
try:
    # code that might throw exception
except UnboundLocalError:
    # Exception handling
except ValueError:
    # Exception handling
except OSError:
    # Exception handling
```

- try-except-else block

Every time, try block runs successfully and no exception is raised, else block gets executed.

```python
'''✨ Python: Try-Except-Else ✨

⚡"Try" successful: Then "try-else" will execute
'''

try:
    print('----- Inside try block -----')
    num = 5 + 5
    print(f"num from try block is: {num}")
except Exception as ex:
    print('----- Inside except block -----')
    print(f'[ERROR]: {ex}')
    num = 2 + 5
else:
    print('----- Inside else block -----')
    num = num + 3
    print(f"num from else block is: {num}")
```

- Finally Block

The finally block will be executed every time after the execution of try, except, and else blocks.

An exception is raised or not, doesn't matter for finally block. It will be executed every time.

So, if there is an exception:

```python
'''✨ Python: Try-Except-Else-Finally ✨

'Try' Fails: Then "except-finally" will execute
'''

try:
    print('----- Inside try block -----')
    num = 'A string' + 5
    print(f"num from try block is: {num}")
except Exception as ex:
    print('----- Inside except block -----')
    print(f'[ERROR CODE 111]:\n{ex}')
    num = 2 + 5
else:
    print('----- Inside else block -----')
    num = num + 3
    print(f"num from else block is: {num}")
finally:
    print('----- Inside finally block -----')
    print(f'Finally num: {num}')
```

if there is no exception:

```python
'''✨ Python: Try-Except-Else-Finally ✨

"Try" successful: Then "try-else-finally" will execute
'''

try:
    print('----- Inside try block -----')
    num = 5 + 5
    print(f"num from try block is: {num}")
except Exception as ex:
    print('----- Inside except block -----')
    print(f'[ERROR CODE 111]:\n{ex}')
    num = 2 + 5
else:
    print('----- Inside else block -----')
    num = num + 3
    print(f"num from else block is: {num}")
finally:
    print('----- Inside finally block -----')
    print(f'Finally num: {num}')
```
