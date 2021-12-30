import json

my_dict = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(json.dumps(my_dict, indent=4))

'''
Output:
{
    "1": {
        "name": "John",
        "age": "27",
        "sex": "Male"
    },
    "2": {
        "name": "Marie",
        "age": "22",
        "sex": "Female"
    }
}
'''

