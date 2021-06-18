'''
Python Filter Function (Basic 1)

Example: Find odd and even numbers 
'''

# Odd filter
def is_odd(n):
    if n % 2 != 0: return True

# Even filter
def is_even(n):
    if n % 2 == 0: return True


numbers = [0, 1, 2, 3, 4, 5]

odd = filter(is_odd, numbers)
even = filter(is_even, numbers)


# Display
print("Odd:", list(odd))
print("Even:", list(even))

'''
Output:
Odd: [1, 3, 5]
Even: [0, 2, 4]
'''
