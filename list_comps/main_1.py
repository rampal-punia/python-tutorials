'''List comprehension Example: Using in place of Map Function.
'''

# Using map and lambda function
emails = ["sachin@gmail.com", "rahul@yahoo.com",
          "dhoni@facebook.com", "rohit@baidu.com", "saurabh@bing.com"]

# names_only = list(map(lambda x: x.split('@')[0], emails))


emails_only = [name.split('@')[1] for name in emails]
print(emails_only)
