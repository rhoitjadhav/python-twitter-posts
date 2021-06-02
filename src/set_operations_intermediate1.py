'''
Python Set (Intermediate 1)

Example: Mathematical Union operation in set
'''
# Create numbers set
num1 = {1, 2, 3}
num2 = {3, 4, 5}


# Using pipe key `|`
ans1 = num1 | num2


# Using union() method
ans2 = num1.union(num2)


# Display
print(ans1)
print(ans2)

'''
Output:
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
'''
