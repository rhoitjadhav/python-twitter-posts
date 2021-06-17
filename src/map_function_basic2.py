'''
Python Map Function (Basic 2)

Example: Find square of numbers 
'''
def square(n):
    return n * n


numbers = [1, 2, 3, 4]

result = map(square, numbers)

# Display
print(list(result))


'''
Output:
[1, 4, 9, 16]
'''

