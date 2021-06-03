'''
Python Set (Intermediate 2)

Example: Mathematical Intersection operation in set
'''
# Create numbers set
num1 = {1, 2, 3, 4}
num2 = {3, 4, 5, 6}


# Using & operator
ans1 = num1 & num2


# Using intersection() method
ans2 = num1.intersection(num2)


# Display
print(ans1)
print(ans2)

'''
Output:
{3, 4}
{3, 4}
'''
