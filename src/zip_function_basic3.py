'''
Python Zip Function (Basic 2)

Example: Unziping the values
'''
numbers = (1, 2, 3)
strings = ("one", "two", "three")

result = zip(numbers, strings)


n, s = zip(*result)

# Display
print("Numbers:", n)
print("Strings:", s)

'''
Output:
Numbers: (1, 2, 3)
Strings: ('one', 'two', 'three')
'''

