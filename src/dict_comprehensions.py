'''
Python Dictionary Comprehensions

Example: 
    - Find and store squares of 1 to 9 numbers 
    in dictionary
'''

# Find squares
squares = {i: i*i for i in range(1, 10)}


# Display the output
for key, value in squares.items():
    print(f"{key} -> {value}")

'''
Output:
1 -> 1
2 -> 4
3 -> 9
4 -> 16
5 -> 25
6 -> 36
7 -> 49
8 -> 64
9 -> 81
'''
