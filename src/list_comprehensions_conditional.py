'''
Python List Comprehensions Conditional
    - Comprehensions in Python provide us with a short and 
    concise way to construct new sequences (such as lists, 
    set, dictionary etc.)
    
    - In the following example we will cover the 
    traditional way and list comprehensive way to create lists

    - Example demonstrates the segregate odd and 
    even numbers from 1 to 10 numbers in empty list
'''

odd = [i+1 for i in range(10) if (i+1) % 2 != 0]

even = [i+1 for i in range(10) if (i+1) % 2 == 0]

print("Odd->", odd)
print("Even->", even)

'''
Output:

Odd-> [1, 3, 5, 7, 9]
Even-> [2, 4, 6, 8, 10]
'''

