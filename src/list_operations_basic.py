'''
Python List (Basic)
    - Store multiple items in single list
    - Mutable datatype
    - Store different kinds of datatypes (e.g. int, str, dict, etc)
    - indexing starts from `0`
'''

# Create numbers list
numbers = [1, 2]

# Add data (append, insert)
numbers.append('3')  # [1, 2, '3']
numbers.append('4')  # [1, 2, '3', '4']
numbers.insert(3, 4)  # [1, 2, '3', 4, '4']

# Update data
numbers[2] = 3  # [1, 2, 3, 4, '4']
numbers[4] = 5  # [1, 2, 3, 4, 5]

# Delete data (remove)
numbers.remove(4)  # [1, 2, 3, 5]
del numbers[3]  # [1, 2, 3]

# View Data
print(numbers)  # [1, 2, 3]
