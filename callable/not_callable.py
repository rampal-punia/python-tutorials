# Int, tuple, list, str objects are not callable
a = 50
print(a(3+4))

a_list = [4, 5, 6]
print(a_list(1))

a_tuple = (1, 2, 3)
print(a_tuple(2))

string = 'Python'
print(string(2))
