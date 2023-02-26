# Python Questions (Strings| Variables| Numbers)

## 1. Do Variables in Python hold the actual data or the reference to that data?

Answer: A variable in Python is a named location in memory that stores a reference to a specific piece of data. When you create a variable in Python, you are creating a reference to the location in memory where the data is stored, rather than the actual data itself.

For example, when you create a variable `x` and assign it the value 5, Python creates a block of memory to hold the value 5 and assigns the name `x` to that memory location.

While variables themselves do not hold the actual data, they do hold a reference to the location in memory where the data is stored. This means that when you create a copy of a list, both the original list and the copy will point to the same data in memory. For example:

```python
original_list = [1, 2, 3]
copy_list = original_list
```

## 2 Define the dynamic typing nature of Python Programming Language

Ans: Dynamic typing is a key feature of Python that allows variables to change data types at runtime. In Python, the data type of a variable is not determined until the program is run, and can change dynamically based on the value it is assigned.

For example, you can create a variable x and assign it an integer value, like so:

```python
x = 5
```

Later on in your program, you can reassign the variable x to a string value:

```python
x = "hello"
```

This is possible because Python uses dynamic typing to determine the data type of a variable based on the value it is assigned. This allows for more flexibility in programming, as you can use the same variable to store different types of data at different times, rather than having to create a new variable for each specific data type.

In contrast to dynamic typing, many other programming languages use static typing, where the data type of a variable is declared at compile time and cannot be changed at runtime. This can be more restrictive, but also provides some benefits, such as better performance and catch errors at compile time rather than runtime.

Python also uses duck typing, which means that the type of an object is determined by its behavior rather than its class. This allows for more flexibility in how objects are used and passed around in the code, and allows for more powerful abstractions.

## 3 What is duck-typing in python?

Ans: In Python, "duck typing" is a programming concept that refers to the ability to use an object based on its behavior rather than its class or Type. This means that Python does not require explicit type declarations for variables, function arguments, or return values. Instead, the type of an object is inferred at runtime based on its behavior.

The term "duck typing" comes from the phrase "if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." For example, if an object has a method called quack(), Python will treat it as a "duck" and allow it to be passed to functions that expect duck-like behavior, regardless of its actual class or type. This makes it easier to write flexible and reusable code that can work with different types of objects.

This means that when you're working with an object in Python, you don't need to know its exact class or type in order to use it. Instead, you can use the object based on the methods and attributes that it provides. For example, imagine you have a function that takes in an object and prints out its length. Here's an example of how you might implement that function using duck typing:

```python
def print_length(obj):
    print(len(obj))
```

In this example, the function doesn't care about the exact class of the object passed in. It only cares that the object has a len() method that can be called to determine its length. As long as the object passed in to the function behaves like a sequence (list, string, tuple, etc), it will work.

Here's an example of how you might use this function with different types of objects:

```python
print_length("hello")  # prints 5
print_length([1, 2, 3, 4, 5])  # prints 5
print_length((1, 2, 3, 4, 5))  # prints 5
```

As you can see, the function is able to work with different types of objects (string, list, tuple) as long as they all have the len() method that can be called.

Duck typing allows for more flexibility in the code, as it allows you to write code that can work with different types of objects, regardless of their exact class. This is particularly useful when working with objects in more advanced features of Python such as polymorphism and decorators, and in general when working with more open-ended and reusable code.

It's also worth mentioning that duck typing is not a feature of Python only, but it's a common pattern in other dynamic languages such as Ruby, JavaScript and others.

## 4 How would you get the memory location of an object in Python

Ans: In Python, you can use the built-in id() function to get the memory address of an object. The id() function takes an object as an argument and returns its unique identifier, which is the memory address where the object is stored.

Here's an example of using the id() function to get the memory address of an integer:

```python
x = 5
print(id(x))
```

This will print a number, that represents the memory location where the value 5 is stored. You can use the `id()` function with any type of object, including lists, strings, and custom classes.

```python
a = [1, 2, 3]
print(id(a))

b = "hello"
print(id(b))

class Person:
    pass

p = Person()
print(id(p))
```

It's important to note that the memory address returned by the id() function is unique for each object, but the same object can have different addresses in different parts of the program. For example, when you create a copy of a list, both the original list and the copy will have different memory addresses.

```python
original_list = [1, 2, 3]
copy_list = original_list.copy()

print(id(original_list))
print(id(copy_list))
```

Also, in python the memory management is done using a garbage collector, so the memory allocated to an object is freed when the object is no longer being used. It's worth mentioning that the value returned by id() is an int and the memory location may change during the lifetime of the object, depending on the python interpreter and the underlying operating system.

Note: While the `id()` function returns the memory address of an object, it's not recommended to use this value for any practical purposes other than comparison. This is because the memory address of an object can change during the lifetime of the program due to factors such as garbage collection or memory management. In general, it's better to rely on the object's properties and methods rather than its memory address.

## 5 What is the maximum length of the integer supported by Python

Ans: In Python, integers are represented using the int type, which can hold arbitrarily large integers. The maximum value of an integer in Python is determined by the amount of memory available on your computer.

The exact maximum value of an integer in Python depends on the implementation of the Python interpreter and the underlying operating system. However, the general rule of thumb is that the maximum value of an integer in Python is about 2^31 - 1 for 32-bit systems and 2^63 - 1 for 64-bit systems.

For example, on a 32-bit system, the maximum value of an integer that Python can represent is 2147483647 (2^31 - 1). You can check this by using the sys.maxsize variable:

```python
import sys
print(sys.maxsize)
```

On a 64-bit system, the maximum value of an integer that Python can represent is 9223372036854775807 (2^63 - 1).

It's worth noting that in Python 3, the int type can be used to represent integers of any size, so the maximum value is essentially limited by the amount of memory available on your computer.

If you need to perform arithmetic with values that are larger than the maximum value of an integer in Python, you can use the decimal module, which provides arbitrary-precision decimal arithmetic.

In practice, you are unlikely to ever hit the limit of integers in Python, and you can use integers as big as you need to for most of use cases.

## 6 Does the symbols like {}, [], () have some type?

Ans: Yes, they are considered as built-in data types in Python.

{} - represents a dictionary, which is an unordered collection of key-value pairs enclosed in curly braces.

For example:

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

[] - represents a list, which is an ordered collection of elements enclosed in square brackets.

For example:

```python
my_list = [1, 2, 3, 'four']
```

() - represents a tuple, which is an ordered collection of elements enclosed in parentheses.

For example:

```python
my_tuple = (1, 2, 'three')
```

In addition to these, there are other built-in data types in Python, such as sets, strings, and numbers, each with their own syntax and behavior.

It's worth mentioning that the parentheses `()` also have a different use as grouping symbols in Python, they are used to indicate the order of operations in mathematical expressions, to group function arguments and can be used to indicate a generator. And also, the square brackets [] are used to indicate list comprehension and indexing.

So, in short, the symbols {}, [], () in Python are used to create different types of data structures and have different meanings depending on the context in which they are used.

## 7 Things to keep in mind while single line assignment for the variables

Ans:

## 8 What is the general convention in Python to declare a Constant?

Ans:

## 9 Define the feature "self-documenting expression with '=' character" added in Python 3.8

Ans:

## 10 How would you print a tab in Python?

Ans:

## 11 If we multiply "Hello" with 10 in Python what output do we get?

Ans:

## 12 From a string "Learning Python Is A Fun" write steps to extract word 'Python'

Ans:

## 13 How would you get the length of a string?

Ans:

## 14 Print all the 'n' from the string ""Learning Python Is A Fun"

Ans:

## 15 What is the difference between capitalize() and title() methods in python strings?

Ans:

## 16 For a given number 72 print the binary octal and hexagonal value

Ans: In Python, you can use the built-in bin(), oct(), and hex() functions to convert an integer to its binary, octal, and hexadecimal representation, respectively.

Here's an example of how you might use these functions to print the binary, octal, and hexadecimal representation of the number 72:

```python
number = 72
print("Binary:", bin(number))
print("Octal:", oct(number))
print("Hexadecimal:", hex(number))

```

output:

```bash
Binary: 0b10010000
Octal: 0o110
Hexadecimal: 0x48
```

As you can see, the output of the bin() function is a string that starts with the prefix 0b, indicating that it's a binary representation. The output of the oct() function starts with the prefix 0o indicating that it's an octal representation, and the output of the hex() function starts with the prefix 0x indicating that it's a hexadecimal representation.

We can also use the `format()` method to convert an integer to a binary, octal, or hexadecimal string representation. Here's an example:

```python
number = 72
print("Binary: {}".format(format(number, 'b')))
print("Octal: {}".format(format(number, 'o')))
print("Hexadecimal: {}".format(format(number, 'x')))

# Output:
Binary: 1001000
Octal: 110
Hexadecimal: 48
```

The 'b', 'o', and 'x' in the format() method represent the format code for binary, octal, and hexadecimal, respectively. The curly braces {} are used as placeholders for the formatted value.

It's worth noting that the bin(), oct(), hex() functions return string representation of the numbers, if you want to use them for mathematical operation you need to convert them back to int using int() function.

## 17 For a given number 82, convert it to bytes and then bytes to the number 82

Ans: In Python, you can use the `int.to_bytes()` method to convert an integer to a bytes object, and the `int.from_bytes()` method to convert a bytes object back to an integer.

Here's an example of how you might use these methods to convert the number 82 to a bytes object, and then back to the number 82:

```python
number = 82

# convert to bytes
bytes_obj = number.to_bytes(1, byteorder='big')
print("Bytes:", bytes_obj)

# convert back to int
original_number = int.from_bytes(bytes_obj, byteorder='big')
print("Original number:", original_number)
```

In this example, the `to_bytes()` method is called with two arguments: the first argument is the number of bytes, in this case 1, and the second argument is the `byteorder`, which is 'big' in this case. The byte order determines the order of the bytes in the bytes object, and it can be either 'big' or 'little'.

The `from_bytes()` method is called with the bytes object and the byte order, which is the same as the original byte order.

The output of the code would be:

```python
Bytes: b'R'
Original number: 82
```

As you can see the `to_bytes()` method returns a bytes object, and when passed to the `from_bytes()` function with the correct byte order it returns the original number.

It's worth noting that when using the `to_bytes()` method, you should specify the appropriate number of bytes required to represent the integer. If the number of bytes is not specified correctly, the resulting bytes object may not represent the original integer.

## 18 Which method of float would you use to check if 11/3 is an integer?

Ans: In Python, you can use the built-in is_integer() method of the float type to check if a float is an integer. The is_integer() method returns True if the float is an integer, and False otherwise.

Here's an example of how you might use the is_integer() method to check if the result of the division 11/3 is an integer:

```python
result = 11/3
if result.is_integer():
    print("The result is an integer.")
else:
    print("The result is not an integer.")
```

In this case, the result of the division 11/3 is 3.6666666666666665 which is not an integer, so the output would be "The result is not an integer."

It's worth mentioning that, when doing the division in Python 3, the division operator / returns a float, even if the operands are integers, so you don't need to cast the result to a float explicitly.

You can also use the math.modf() function to check if a float is an integer. It returns a tuple containing the fractional and integer parts of a float. If the fractional part is 0, the number is an integer.

```python
import math
result = 11/3
if math.modf(result)[0] == 0:
    print("The result is an integer.")
else:
    print("The result is not an integer.")
```

Another way is to use the int() function, when the float is casted to an int the decimal part is truncated, so if the original float and the casted int are equal the number is an integer

```python
result = 11/3
if int(result) == result:
    print("The result is an integer.")
else:
    print("The result is not an integer.")
```

In all the above methods, you can use the result variable and check if it is an integer or not.

## 19 join all the items of this list ["Learning", "Python", "Is", "Fun"]

Ans: In Python, you can use the join() method of the string class to join all the items of a list into a single string. The join() method takes an iterable (such as a list) as an argument, and returns a string that is formed by concatenating the elements of the iterable, separated by the string on which the method is called.

Here's an example of how you might use the join() method to join all the items of the list ["Learning", "Python", "Is", "Fun"] into a single string:

```python
my_list = ["Learning", "Python", "Is", "Fun"]
result = " ".join(my_list)
print(result)
```

This will output the string: "Learning Python Is Fun".

In this example, the join() method is called on a string containing a single space, and the argument is the list of strings. The result is a new string that is formed by concatenating the elements of the list, separated by the space.

You can use any separator instead of the space, for example, you could use "_" to join the list items like this:

```python
result = "_".join(my_list)
```

This would output the string: "Learning_Python_Is_Fun"

It's worth noting that the join() method is called on the separator string and not the list, this is the opposite of the split() method that is called on the string and not the separator.

## 20 What would be output of the below code?

Ans: print(False + 1.5)
print(True + 1.5)
In this code, the + operator is used to add the value of the False boolean to the value of the 1.5 float. In Python, the False boolean is treated as the integer value 0 when used in a mathematical operation, so the expression False + 1.5 is equivalent to 0 + 1.5, which evaluates to 1.5.

It's worth noting that Boolean values in Python can be used in numerical contexts, which is why you can use the + operator on the boolean value False.

It's also worth mentioning that the same thing applies for the True boolean, it is considered as 1 when used in a mathematical operation.

## 21 What is the length of '\n' and  r'\n'

Ans: In Python, the string '\n' represents a newline character, which is a special character used to indicate the end of a line of text. This character is represented by a backslash \ followed by the letter n.

When you use the built-in len() function to get the length of the string '\n', it returns 1. This is because the len() function returns the number of characters in the string, and the string '\n' contains only one character: the newline character.

It's important to note that the newline character is not visible when you print a string that contains it, but it is still considered to be a character. This can be seen when you use the string in a file, the newline character will separate the string from the next one.

Here's an example to illustrate this:

```python
s = 'hello\nworld'
print(len(s))  # prints 11
```

As you can see in the example above, the length of the string s is 11, which includes the newline character.

It's also worth noting that the \n character is also considered one character when used in a string, and that it may have different behavior depending on the platform you are working on, as different operating systems have different conventions for newline characters. In Windows

If you use the len() function on the raw string r'\n', it will return 2. This is because a raw string in Python is a string that is specified using the r prefix before the opening quotation mark. Raw strings are not interpreted by the Python interpreter, so any special characters (like \n) in a raw string are treated as literal characters.

In the case of r'\n', the backslash \ is treated as a literal character and is included in the length of the string. So, when you use the len() function on the raw string r'\n', it returns 2, which is the number of characters in the string: the backslash \ and the letter n.

Here's an example to illustrate this:

```python
s = r'\n'
print(len(s))  # prints 2
```

This is usually not the behavior you are looking for when working with newline characters, so it's more common to use the string '\n' to include a newline character in a string, rather than using a raw string.

It's worth noting that using raw strings could be useful when you need to include special characters such as backslashes in a string without having them to be interpreted by the Python interpreter, like in regular expressions, file paths or when the string contains escape sequences that you want to keep as-is.

## 22 if string = "abcdcdc" and substring = "cdc" then find number of times substring present in string

Ans: You can use the str.count() method to find the number of times a substring appears in a string, including overlapping occurrences.

```python
string = "abcdcdc"
substring = "cdc"
count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1
print(count)
```

This will output 2, the substring "cdc" appears twice in the string "abcdcdc"

The above code uses a for loop to iterate over the string, and check if the substring is present at the current position, by comparing the slice of the string starting at the current position with the length of the substring, to the substring.

It's worth noting that this approach is less efficient than using the re module, but is simple and easy to understand for this specific problem.

## 23  any and all functions

Ans: ```python
if __name__ == '__main__':
    s = "aA2"
    has_alpha = any(c.isalpha() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

```

In this modified code, I've used the built-in string methods isalpha(), isdigit(), islower(), and isupper() to check for the presence of alphabets, digits, lowercase letters, and uppercase letters respectively. These methods returns True if the character is an alphabet, digit, lowercase letter, or uppercase letter respectively, otherwise returns False.

Then using any() function to check if any of the characters in the string are of the given type.

It eliminates the need for multiple for loops and makes the code more efficient by checking for all possible conditions in a single line.

It's worth mentioning that this solution is more readable and efficient than the original code.
