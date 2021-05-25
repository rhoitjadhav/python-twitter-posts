'''
Python Tuples with Multiple Datatype

Example: Store and print int, string, list 
         elements
'''

# Create numbers tuple
items = (
    1, 2,
    "abc", "def",
    [5, 6]
)

for item in items:
    type_of_item = type(item).__name__
    print(f"{type_of_item} -> {item}")


'''
Output:
int -> 1
int -> 2
str -> abc
str -> def
list -> [5, 6]
'''
