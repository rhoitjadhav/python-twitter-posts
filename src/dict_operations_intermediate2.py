'''
Python Dictionary (Intermediate 2)
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

# get() method in Dictionary 
print(student.get('address', 'Not exists'))

print(student['address'])


'''
Output:
Not exists
Traceback (most recent call last):
  File "test/test.py", line 18, in <module>
    print(student['address'])
KeyError: 'address'
'''
