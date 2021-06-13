'''
Python f-strings format datetime

Example: Print current date
'''
from datetime import datetime


# Current datetime
now = datetime.now()


# Display
print(f'{now: %d-%m-%Y}')


'''
Output:
13-06-2021
'''

