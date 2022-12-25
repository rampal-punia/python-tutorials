# *args, **kwargs

## Use

Generally we can pass only, as many numbers of arguments to a function, as the number of parameters placed, during the `function declaration`.

```python
# A function to add two variables. (Parameters: a, b)
def add(a, b):
    return a + b

# Calling the function with arguments. 
print(add(2, 3))
# Output: 5
```

Here, We can not pass more than 2 arguments. Therefore this `add` function can return the result for only 2 variables.  As only two parameters are declared here, `a, b`.

So, what if we need to add more than 2 variables, or any desired numbers of variables. We need a placeholder that can accumulate as many arguments as required by the user. This is a very simple case scenario here. But I hope you get the point.

Here comes `*args` and `**kwargs` to rescue. With the help of  `*args and **kwargs` we can pass as many arguments as we like. They work as the placeholder for any number of variables.

Let's look at the `*args` first.

### *args

Passing `any number of positional arguments` to a function.

The above `add` function can be modified with the help of args.

```python
# A function to add any number of variables.
def add_numbers(*args):
    return sum(args)

# Passing as many numbers of arguments as required.
print(add_numbers(2, 3, 4, 5, 6, 7, 8, 9, 11))
# Output: 55
```

### **kwargs

Example: Without `**kwargs`.

```python
student_marks = {}


def add_student_marks(name, marks):
    student_marks[name] = marks


add_student_marks('Rahul', 80)
add_student_marks('Arun', 85)
print(student_marks)
```

We need to call the `add_student_marks` function twice to add 2 students.

### Add multiple students with single function call

Passing `any number of keyword arguments` to a function:

Let's modify the same `add_student_marks` function to receive any number of students in a single function call. The above function can be modified to accept any number of keyword arguments with the help of `**kwargs`.

Example: With `**kwargs`.

```python
student_marks = {}


def add_student_marks(**marks):
    for name, marks in marks.items():
        student_marks[name] = marks


add_student_marks(Rahul=80, Arun=85, Kishore=90, Anju=91)
print(student_marks)

```

---

## What data structures do `*args & **kwargs` hold?

To check this we use the in-built `type` function:

```python
print(type(args))
# Output: <class 'tuple'>

print(type(kwargs))
# Output: <class 'dict'>
```

So, we can say `args` refers to a `tuple` and `kwargs` refers to a `dictionary`.

---

## Once placed as parameters in a function, are they become required or optional parameters?

They remains the optional parameters.

---

## Does the name `args` and `kwargs` matters?

No the name args & kwargs does not matter here.

Instead of `args` and `kwargs` we can use any name for these variable. Only the number of asterisks matters. One asterisk `*` before any variable_name makes it a `tuple`, and two asterisks `**` before any variable_name make it a dictionary.
