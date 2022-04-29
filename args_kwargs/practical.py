def get_pizza_order(order_num, size, *toppings, **kwargs):
    print("===============================================")
    print(f"Order number: {order_num}")
    print(f"Preparing pizza with size {size} inches.")

    if toppings:
        print("Adding the following toppings to the pizza.")
        for topping in toppings:
            print(f" - {topping}")

    if kwargs:
        for k, v in kwargs.items():
            print(f"{k} : {v}")
    print("===============================================")

# 'green chilly', 'mushroom', 'extra cheese',
# 'extra paneer', 'Italian sausage', 'pepperoni'


order_1 = get_pizza_order(110,
                          7,
                          'green chilly',
                          'mushroom',
                          'extra cheese',
                          delivery_type="Home",
                          address="abc, xyz road",
                          ph_num=8888888888
                          )

order_2 = get_pizza_order(111,
                          10,
                          'green chilly',
                          'mushroom',
                          'extra cheese',
                          'pepperoni',
                          table_num=12,
                          ph_num=8888888887
                          )
order_3 = get_pizza_order(112,
                          10,
                          'extra paneer',
                          'Italian sausage',
                          'pepperoni',
                          'extra cheese',
                          'pepperoni',
                          table_num=12,
                          ph_num=8888888887,
                          tip="more than required"
                          )
