'''
Python Set (Intermediate 4)

Example: Mathematical Symmetric Difference operation in set
'''
# Create numbers set
num1 = {1, 2, 3, 4}
num2 = {3, 4, 5, 6}


# Using ^ operator
ans1 = num1 ^ num2


# Using symmetric_difference() method
ans2 = num1.symmetric_difference(num2)


# Display
print(ans1)
print(ans2)

'''
Output:
{1, 2, 5, 6}
{1, 2, 5, 6}
'''

