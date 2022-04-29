'''Map function example -2: Get names only from a list of emails.
'''

emails_list = ["sachin@gmail.com", "rahul@yahoo.com",
               "dhoni@facebook.com", "rohit@baidu.com", "saurabh@bing.com"]


# names_only = list(map(lambda x: x.split('@')[0], emails_list))
emails_only = list(map(lambda x: x.split('@')[1], emails_list))

print(emails_only)
