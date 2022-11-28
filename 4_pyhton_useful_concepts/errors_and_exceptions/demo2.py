'''✨ Python: Try-Except-Else-Finally ✨

2: try succeeds
'''

try:
    a = 5 + 5
except Exception as ex:
    print('Inside except block')
    print(f'[ERROR]: {ex}')
    a = 2 + 5
else:
    print('Inside else block')
    a = a + 3
finally:
    print(f'Finally a: {a}')
