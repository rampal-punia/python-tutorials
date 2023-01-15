'''✨ Python: Try-Except-Else-Finally ✨

'Try' Fails: Then "except-finally" will execute
'''

try:
    print('----- Inside try block -----')
    num = 'A string' + 5
    print(f"num from try block is: {num}")
except Exception as ex:
    print('----- Inside except block -----')
    print(f'[ERROR CODE 111]:\n{ex}')
    num = 2 + 5
else:
    print('----- Inside else block -----')
    num = num + 3
    print(f"num from else block is: {num}")
finally:
    print('----- Inside finally block -----')
    print(f'Finally num: {num}')
