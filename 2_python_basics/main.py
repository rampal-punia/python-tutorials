'''📝 Example codes used in readme.md (Python Basics)

✨ Uncomment, Run and Check the output
'''

#### Examples of variables ####

# developer_name = "Rahul"        # string
# age = 30                        # int
# experience_in_years = 5.8       # flaot
# programming_language = "Python"  # string
# is_on_leave = False             # boolean

#### Dynamically typing ####
# a = 'Rahul'             # referencing string
# a = 100                 # referencing int
# a = 150.25              # referencing float
# a = [1, 2, 3, 4, 5]     # referencing list

#### Checking the ids of the variable ####
# developer_name = "Rahul"
# print(id(developer_name))       # 140549527402160

# age = 100
# print(id(age))                  # 9804416

# experience_in_years = 150.25
# print(id(experience_in_years))  # 140118263398640

# is_on_leave = False
# print(id(is_on_leave))          # 9486304

# # But in case of list.

# b = [1, 2, 3, 4, 5]
# print(id(b))                    # 140118263437440

# # if we append the list the id remains same and the list get appended to the same memory location
# b.append(6)
# print(id(b))                    # 140118263437440

#### Checking the type of the variable ####
# a = 'Python'
# print(type(a))          # <class 'str'>

# a = 100
# print(type(a))          # <class 'int'>

# a = 150.25
# print(type(a))          # <class 'float'>

# a = [1, 2, 3, 4, 5]
# print(type(a))          # <class 'list'>

# Check the type of function type
# print(type(type))         # <class 'type'>

s = "I am learning Python Programming language"
print(s.split())
