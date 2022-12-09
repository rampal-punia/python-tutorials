'''📝 Example codes used in readme.md (Python Basics)

✨ Uncomment, Run and Check the output
'''
x = 56000/100
y = 56
z = 56 + 5j
a = 7
b = b'\x07\x00'
print([item for item in dir(y) if not item.startswith('_')])
print(x.as_integer_ratio())
print(y.denominator)
print(y.numerator)
print(y.bit_length())
print(z.conjugate())
print(z.imag)


print(a.to_bytes(2, 'little'))
print(int.from_bytes(b, 'little'))
