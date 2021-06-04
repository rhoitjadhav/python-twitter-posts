'''
Python Set (Intermediate 3)

Example: Mathematical Difference operation in set
'''
# Create numbers set
num1 = {1, 2, 3, 4}
num2 = {3, 4, 5, 6}


# Using - operator
ans1 = num1 - num2


# Using difference() method
ans2 = num1.difference(num2)


# Display
print(ans1)
print(ans2)

'''
Output:
{1, 2}
{1, 2}
'''
