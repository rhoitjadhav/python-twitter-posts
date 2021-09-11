'''
Python Exception Handling (Basic 2)

Example: exception handling examples
'''
try:
    1/0

except Exception as e:
    print(repr(e))


'''
Output:
ZeroDivisionError('division by zero')
'''

