'''
Python Zip Function (Basic 2)

Example: Zip function examples
'''
numbers = (1, 2, 3)
strings = ("one", "two", "three")

result = zip(numbers, strings)

# Display
for r in result:
    print(r)

'''
Output:
(1, 'one')
(2, 'two')
(3, 'three')
'''

