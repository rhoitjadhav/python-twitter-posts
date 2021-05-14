'''
Python Dictionary (Intermediate 1)
    - It's an unordered collection of items
    - Mutable Datatype
    - Key/Value pair data structure
'''

# Create dictionary of student
student = {
    'name': 'Alex Hales',
    'age': 25,
    'dob': '10/04/1996'
}


# Get keys
keys = list(student.keys())
print("Keys:", keys)


# Get values
values = list(student.values())
print("Values:", values)

'''
Output:
Keys: ['name', 'age', 'dob']
Values: ['Alex Hales', 25, '10/04/1996']
'''
