import json

json_string = '{"name": "Kevin Durant", "age": 33}'

# Convert to dict
dictionary = json.loads(json_string)

print(type(dictionary))
print(dictionary)

'''
Output:

<class 'dict'>
{'name': 'Kevin Durant', 'age': 33}

'''
