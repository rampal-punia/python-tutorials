'''📝 Python Zip function

✨ Convert 2 lists into a dictionary
'''

l1 = ['fname', 'lname', 'age', 'language']
l2 = ['John', 'Doe', 30, 'Python']

data1 = dict(zip(l1, l2))
print(data1)


l3 = ['Mary', 'Jane', 30, 'JavaScript']
data2 = dict(zip(l1, l3))
print(data2)
