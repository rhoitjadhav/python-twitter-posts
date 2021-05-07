'''
Python List (Advanced 1)
    - Store multiple items in single list
    - Mutable datatype
    - Store different kinds of datatypes (e.g. int, str, dict, etc)
    - indexing starts from `0`
'''

# Create numbers list
numbers = [0, 1, 2, 3, 4]


# List Slicing

# Get all numbers in list
print(numbers[:])  
# O/P: [0, 1, 2, 3, 4]

# Get numbers from index 1 to 3, 
print(numbers[1:4])
# O/P: [1, 2, 3]

# Reverse the list
print(numbers[::-1])
# O/P: [4, 3, 2, 1, 0]

# Get numbers from index 4 to 1 in reverse order
print(numbers[5:0:-1])
# O/P: [4, 3, 2, 1]

