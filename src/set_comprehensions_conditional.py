'''
Python Set Comprehensions Conditional

Example: Find odd and even numbers from 0 to 9
'''

odd = {i for i in range(10) if (i % 2) != 0}

even = {i for i in range(10) if (i % 2) == 0}


# Display
print(odd)
print(even)

'''
Output:
{1, 3, 5, 7, 9}
{0, 2, 4, 6, 8}
'''

