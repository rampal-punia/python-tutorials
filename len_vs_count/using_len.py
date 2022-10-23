'''Python Tutorial: Using len function
'''

an_str = "Hello world"
print(len(an_str))

# Just to demonstrate that python internally calls the
# __len__ method. We should not call this method directly.
# Use len(a_container) syntax instead.
print(an_str.__len__())

a_tuple = (0, 1, 2, 3, 4, 5, 6, 7)
print(len(a_tuple))

a_list = ['a', 'd', 'k', 'm', 'o']
print(len(a_list))

a_dict = {"id": 21123, "name": "John", "age": 21}
print(len(a_dict))

a_set = {3, 45, 75, 34, 44}
print(len(a_set))
