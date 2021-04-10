'''
Python List (Intermediate)
    - Store multiple items in single list
    - Mutable datatype
    - Store different kinds of datatypes (e.g. int, str, dict, etc)
    - indexing starts from `0`
'''
# Create colors lists
colors = ['red', 'blue', ]
new_colors = ['green', 'white']

# Combine two lists (extend)
colors.extend(new_colors)
# O/P: ['red', 'blue', 'green', 'white']

# Reverse the order of elements on the list (reverse)
colors.reverse()
# O/P: ['white', 'green', 'blue', 'red']

# Sort the elements in the list (sort)
colors.sort()
# O/P: ['blue', 'green', 'red', 'white']

# Remove all the elements of the list (clear)
colors.clear()
# O/P: []
