def func(*toppings, **address):
    return type(toppings), type(address)


ord1 = func('green chilly', 'mushroom', house_num=123, city='abc')
print(ord1)
