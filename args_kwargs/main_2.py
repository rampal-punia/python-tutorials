def func(name, *toppins, **address):
    print(f"Welcome, {name}")
    print(type(toppins))
    print(type(address))
    if toppins:
        print(toppins)
    if address:
        print(address)


user_1 = func("Sachin")
print(user_1)
