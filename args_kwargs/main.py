'''Code related to the args, kwargs readme file.
'''


def add(a, b):
    return a + b


def add_numbers(*args):
    print(type(args))
    return sum(args)


def display_name(fname="John", lname="Doe"):
    print(fname, lname)


def display(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k} : {v}")


# print(add(8, 7))
print(add_numbers(2, 3, 4, 5, 6, 7, 8, 9, 11))

print(display_name(lname="Jane", fname="Mary"))
print(display(lname="Jane", fname="Mary",
      address="XYZ city", ph_num="123456789", pin="111111"))
