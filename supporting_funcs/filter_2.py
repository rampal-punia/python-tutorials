'''Filter function example to filter only odd from a list.
'''

numbers = [458, 569, 1254, 3652, 562, 2541, 889, 568, 997, 542, 325]

odd_num_list = list(filter(lambda x: x % 2 == 1, numbers))

print(odd_num_list)
