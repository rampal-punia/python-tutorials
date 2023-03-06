# a, b = 14, 9
# # Using in a tuple
# # Syntax: (false_value, true_value)[test]
# value = (a, b)[a > b]
# print(value)

a, b = 5, 10
(a, b)[a > b]
print((a, b)[a > b])  # 5
