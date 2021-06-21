'''
Python Eval Function (Basic 2)

Example: Eval function examples 
'''
# Square Function
def square(n):
    return n ** 2


globals = {
    "sqrt": square
}


result = eval("sqrt(10)", globals)

# Display
print("Square:", result)


'''
Output:
Square: 100
'''

