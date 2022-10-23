'''Python Tutorial Series: Sorted() VS Sort()
'''
any_list = [31, 24, 73, 88, 12]
print(any_list)

any_list.sort()
print(any_list)
'''
1. Sorted is a function. it takes iterables like str, list, 
tuple and dictionary
whereas sort is a method only for the list

2. sorted returns a list can be captured in a variable 
and used as and when required.
whereas sort returns none.

3. Sorted is not in -place hence time taken by it is 
more than sort as sort is in-place(i.e. the list itself 
is modified)

'''
