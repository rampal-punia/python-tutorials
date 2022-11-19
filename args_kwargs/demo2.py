def prepare_pizza(order_num, size, *toppings):
    """📝 A function to print order details for the pizza to be prepared.

    We can receive as many toppings as required by the customer with
    the help of *args. 

    Args:
        order_num (int): A unique number to identify the order
        size (int): Size of the pizza
        topping (tuple): tuple containing required toppings name
    """

    print(f"Order number: {order_num}")
    print(f"Pizza size: {size} inches.")

    print("Preparing pizza with following toppings.")
    for topping in toppings:
        print(f" - {topping}")


def delivery_address(**address):
    print("To be delivered at the following address.")
    for k, v in address.items():
        print(f" - {k} : {v}")


def deliver_pizza(name, order_num, size, *toppings, **address):
    print(f"Order for: {name}")
    print("------------------------------------")
    print("toppings 123", toppings)
    prepare_pizza(order_num, size, *toppings)
    delivery_address(**address)


# Method:1️⃣ - To call this function
selected_size = 10
ord1 = deliver_pizza('Sachin',
                     1001,
                     selected_size,
                     'green chilly',
                     'mushroom',
                     'extra cheese',
                     house_num=123,
                     city='abc',
                     pin=123456
                     )
print(ord1)
print("-----------------------------------------------------------")

# Method:2️⃣ - To call this function
user_toppings = ('Pepperoni', 'Sausage', 'Green pepper')
user_address = {'house_num': 456, 'city': 'xyz', 'pin': 456789}
selected_size = 10
ord1 = deliver_pizza('Arjun',
                     1002,
                     selected_size,
                     *user_toppings,
                     **user_address
                     )
print(ord1)
