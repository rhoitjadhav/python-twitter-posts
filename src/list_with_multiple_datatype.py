'''
Python List with multiple datatypes

Example: Store and print int, string dict 
        elements list
'''

# Create list of int, string, dict elements
items = [
    1, 2,
    "abc", "def",
    {"name": "Siri"}
]

for item in items:
    type_of_item = type(item).__name__
    print(f"{type_of_item} -> {item}")


'''
Output:
int -> 1
int -> 2
str -> abc
str -> def
dict -> {'name': 'Siri'}
'''
