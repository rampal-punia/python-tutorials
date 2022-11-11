my_list = ['Python', 'Java', 'JavaScript', 'C', 'Go']
print(sorted(my_list, key=len)[-1])

# or

print(max(my_list, key=len))
