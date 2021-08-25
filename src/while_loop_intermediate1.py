'''
Python While Loop (Intermediate 1)

Example: while loop examples
'''
cubes = {}

i = 0
while i < 5:
    cubes[i] = i ** 3
    i += 1


i = 0
while i < 5:
    print(f"{i}: {cubes[i]}")
    i += 1

'''
Output:
0: 0
1: 1
2: 8
3: 27
4: 64
'''

