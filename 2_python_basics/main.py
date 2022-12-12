'''📝 Example codes used in readme.md (Python Basics)

✨ Uncomment, Run and Check the output
'''
# Prompt user to enter their age. Convert the string into integer, using int()
# age = int(input("Enter your age: "))
# print(f"You will be {age+10} years old after 10 years.")

# Use str.isdigit().
# This method returns True if all characters in the string are digits.
# age = (input("Enter your age: "))

# if age.isdigit():
#     age = int(age)
#     print(f"You will be {age+10} years old after 10 years.")
# else:
#     print("Invalid input")

# Use try-except block
age = (input("Enter your age: "))

try:
    age = int(age)
    print(f"You will be {age+10} years old after 10 years.")
except Exception as ex:
    print("[ERROR]", ex)
