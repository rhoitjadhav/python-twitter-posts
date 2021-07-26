'''
Python Commandline arguments (Basic 2)

Example: Iterate through commandline arguments 
'''
import sys

args = sys.argv


for i in range(len(args)):
    print(args[i])

'''
Output:
test.py
arg1
arg2
'''

