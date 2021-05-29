'''
Python Tuple Slicing 

Example: Create tuple, print first & last 3 numbers 
         along with reverse ordered tuple

'''

# Create numbers tuple
numbers = (0, 1, 2, 3, 4)


# Display
print("First 3 numbers:", numbers[:3])

print("Last 3 numbers:", numbers[-3:])

print("Reverse Order:", numbers[::-1])


'''
Output:
First 3 numbers: (0, 1, 2)
Last 3 numbers: (2, 3, 4)
Reverse Order: (4, 3, 2, 1, 0)
'''
