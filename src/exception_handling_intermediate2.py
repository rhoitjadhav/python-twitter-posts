'''
Python Exception Handling (Intermediate 2)

Example: exception handling examples
'''
import traceback

try:
    # ---Some Code--- 

    raise Exception("Custom Exception raised")

except Exception as e:
    traceback.print_exc()


'''
Output:
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    raise Exception("Custom Exception raised")
Exception: Custom Exception raised
'''

