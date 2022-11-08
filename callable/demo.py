def some_func(a):
    return 2 * a


print(callable(some_func))
# Output: True


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __call__(self):
        return self.fname, self.lname

    def display(self):
        print(self.fname, self.lname)


print(callable(Person))

p = Person("John", "Doe")
print(callable(p))
print(callable(p.display))
