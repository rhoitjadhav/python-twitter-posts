'''
Python Exception Handling (Intermediate 1)

Example: exception handling examples
'''
import traceback

try:
    # ---Some Code--- 
    print(1/0)

except Exception as e:
    traceback.print_exc()


'''
Output:
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    print(1/0)
ZeroDivisionError: division by zero
'''

