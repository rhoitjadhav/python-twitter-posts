'''
Python List Comprehensions
    - Comprehensions in Python provide us with a short and 
    concise way to construct new sequences (such as lists, set, dictionary etc.)
    
    - In the following example we will cover the traditional way and list comprehensive way
    to create lists

    - Example demonstrates the adding 1 to 10 numbers in empty list
'''

# Old Way
old = []

for i in range(10):
    old.append(i+1)

print("Old->", old)

# New Way (List Comprehesions)
new = [i + 1 for i in range(10)]

print("New->", new)

'''
Output: 

Old-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
New-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

