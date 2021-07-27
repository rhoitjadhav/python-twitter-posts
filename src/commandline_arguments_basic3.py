'''
Python Commandline arguments (Basic 3)

Example: Arithmatic operations  
'''
import sys

args = sys.argv


addition = 0

for i in range(1, len(args)):
    addition += int(args[i])

print("Addition:", addition)

'''
$ python test.py 2 3 4


Output:
Addition: 9

'''

