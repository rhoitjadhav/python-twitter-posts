'''
Python Accepting User Input (Intermediate 2)

Example: input() function examples
'''

numbers = list(map(int, input("Enter number: ").split()))

addition = 0 


for number in numbers:
    addition += number

print(f"Addition: {addition}")


'''
Output:
Enter number: 1 2 3 4
Addition: 10
'''

