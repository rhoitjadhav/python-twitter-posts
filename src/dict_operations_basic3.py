'''
Python Dictionary (Basic 3)
    - It's an unordered collection of items
    - Mutable Datatype
    - Key/Value pair data structure
'''

# Create dictionary of student
student = {
    'name': 'Alex Hales',
    'age': 25,
    'dob': '10/04/1996',
    'address': 'London',
    'phone': 9876543210,
}

# Remove using `pop()`
student.pop('phone')  # Returns: 9876543210


# Remove using `del` keyword
del student['address']


# Remove using `popitem()`
student.popitem()  # Returns: ('dob', '10/04/1996')


# Display dictionary
print(student)

'''
Output:
{
    'name': 'Alex Hales', 
    'age': 25
}
'''
