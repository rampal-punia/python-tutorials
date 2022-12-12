# Input Function (Taking input from a user)

The input() function in Python is used to receive the input from the user through the console. The input function reads a string from standard input. We can store the string entered by user in a variable and use further in our code.

```python
username = input("Enter your name: ")
print(f"Hello, {username}!")
```

This code will prompt the user to enter their name. The entered name will be stored in the `username` variable. The program will then print a greeting to the user using the entered name.

One thing to remember while using the `input()` function in Python, is that, it will always return a string.

```python
username = input("Enter your name: ")
print(type(username))

# Output (After the input from user)
<class 'str'>

# This means the input function after returns a string.
```

We need to convert the user input from str to integer (if required in the code). There are several ways to do so.

For example:

```python
# Prompt user to enter their age. 
# 1. Convert the string into integer, using int()
age = int(input("Enter your age: "))
print(f"You will be {age+10} years old after 10 years.")

# 2. Use str.isdigit().
# This method returns True if all characters in the string are digits.
age = (input("Enter your age: "))

if age.isdigit():
    age = int(age)
    print(f"You will be {age+10} years old after 10 years.")
else:
    print("Invalid input")

# 3. Use try-except block
age = (input("Enter your age: "))

try:
    age = int(age)
    print(f"You will be {age+10} years old after 10 years.")
except Exception as ex:
    print("[ERROR]", ex)
```
