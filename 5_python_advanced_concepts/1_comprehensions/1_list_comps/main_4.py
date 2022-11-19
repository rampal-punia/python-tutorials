'''List comprehension Example: Using in place of Map Function.
'''

# Using map and lambda function
# emails = ["sachin@gmail.com", "rahul@yahoo.com",
#                "dhoni@facebook.com", "rohit@baidu.com", "saurabh@bing.com"]

# names_only = list(map(lambda x: x.split('@')[0], emails))

# print(names_only)

# Using list comprehension

emails = ["sachin@gmail.com", "rahul@yahoo.com",
          "dhoni@facebook.com", "rohit@baidu.com", "saurabh@bing.com"]

names_only = [email.split('@')[0] for email in emails]
print(names_only)
