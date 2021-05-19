'''
Python Nested List

Example: 
    - Create and print 3*3 matrix
'''

# Create 3*3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Print Matrix
for i in range(3):
    print(*matrix[i])

'''
Output:
1 2 3
4 5 6
7 8 9
'''
