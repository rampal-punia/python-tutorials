# *args, **kwargs

## Use
Generally we can pass as many arguments to a function as the parameters placed during the function declaration.

```python
# A python function to add two variables
def add(a, b):
    return a + b

print(add(2, 3))
# Output: 5
```

We can not add three or four or some other number of variables with the help of this function. As only two parameters are declared here, `a, b`. This is a very simple scenerio here. But I hope you get the point. 

But with the help of args we can pass as many arguments as we like. 


### *args
Pass `any number of arguments` to a function. The above function can be modified with the help of args.
```python
# A python function to add any number of variables.
def add_numbers(*args):
    return sum(args)

print(add_numbers(2, 3, 4, 5, 6, 7, 8, 9, 11))
# Output: 55
```


### **kwargs
Pass `any number of keyword arguments` to a function.
```python
def display_name(fname="John", lname="Doe"):
    print(fname, lname)

# Notice we are passing lname first and fname second.
# But the output will be correct, as they are keyword arguments
print(display_name(lname="Jane", fname="Mary"))
# Output: Mary Jane
```

The above function can be modified to accept any number of keyword arguments.
```python
def display(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

print(display(lname="Jane", fname="Mary",
      address="XYZ city", ph_num="123456789", pin="111111"))

```
---

## What data structures they hold?
To check this we do:
```python
# Inside function add_numbers
print(type(args))
# Output: <class 'tuple'>

# Inside function display
print(type(kwargs))
# Output: <class 'dict'>
```

So, we can say args refers a tuple and kwargs refers a dictionay.

---

## Once placed as parameters in a function, are they become required or optional parameters?
They remains the optional parameters.

---

## Does the name of args and kwargs matters? 

No, instead of args and kwargs we can use any name for these variable. Only the number of asterisks matters. one asterisk before any name (*) makes it a tuple, and two asterisks (**) make before any variable makes it a dictionary.


