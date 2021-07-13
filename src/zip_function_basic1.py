'''
Python Zip Function (Basic 1)

Example: Zip function examples
'''
numbers = (1, 2, 3)
strings = ("one", "two", "three")

result = zip(numbers, strings)

# Display
print(dict(result))

'''
Output:
{1: 'one', 2: 'two', 3: 'three'}
'''

