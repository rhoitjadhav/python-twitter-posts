'''
Python Dictionary (Basic 4)
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


# Iterate through dictionary
for key, value in student.items():
    print(f"{key}: {value}")


'''
Output:
name: Alex Hales
age: 25
dob: 10/04/1996
'''
