'''
Python Nested Dictionary

Example: 
    - Create and print nested dictionary
'''

# Student details
student = {
    "name": "Steph Curry",
    "age": 33,
    "address": {
        "city": "Akron",
        "country": "United States"
    }
}

# Print student details
print("Name:", student['name'])
print("Age:", student['age'])
print("City:", student['address']['city'])
print("Country:", student['address']['country'])


'''
Output:
Name: Steph Curry
Age: 33
City: Akron
Country: United States
'''
