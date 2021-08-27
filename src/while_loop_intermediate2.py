'''
Python While Loop (Intermediate 2)

Example: while loop examples
'''
words = []

print("Enter 3 words")

i = 0
while i < 3:
    word = input()
    words.append(word)

    i += 1


print("Words:", words)

'''
Output:
Enter 3 words
What
Why
How
Words: ['What', 'Why', 'How']
'''

