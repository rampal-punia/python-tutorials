def func(*toppings, **address):
    """📝 A function to check the type of args and kwargs

    Returns:
        type: type of args and kwargs
    """
    return type(toppings), type(address)


ord1 = func('green chilly', 'mushroom', house_num=123, city='abc')
print(ord1)
