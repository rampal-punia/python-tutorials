def prepare_pizza(order_num, size, topping1, topping2):
    """A function to print order details for the pizza to be prepared.
    While receiving an order from the customer with this function, 
    we can add only 2 toppings. So, this is the limitation of this function.
    We will improve it using *args and **kwargs further but first,
    let's understand how it works without *args and **kwargs. 

    Args:
        order_num (int): A unique number to identify the order
        size (int): Size of the pizza
        topping1 (str): topping name 1
        topping2 (str ): topping name 2
    """
    print(f"Order number: {order_num}")
    print(f"Preparing pizza with size {size} inches.")

    print("Adding the following toppings to the pizza.")
    print(f" - {topping1}")
    print(f" - {topping2}")


order_1 = prepare_pizza(110, 7, 'green chilly', 'mushroom')
order_2 = prepare_pizza(111, 10, 'cheese', 'cucumber')
