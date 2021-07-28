'''
Python Commandline arguments (Intermediate 1)

Example: Argument Seperator
'''
import sys

args = sys.argv

print(args)

'''
$ python test.py Hello World
$ python test.py "Hello World"

Output:
1st Command: ['test.py', 'Hello', 'World']
2nd Command: ['test.py', 'Hello World']
'''

