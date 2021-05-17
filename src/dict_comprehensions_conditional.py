'''
Python Dictionary Comprehensions Conditional

Example: 
    - Remove students with marks less than 40
'''

# Students Marks
students = {
    "Mark": 40,
    "Davis": 50,
    "James": 70,
    "Alex": 30,
    "Kyle": 39
}

# Get students with marks more than 39
passed = {k: v for k, v in students.items() if v > 39}


# Display the output
for k, v in passed.items():
    print(f"{k} -> {v}")


'''
Output:
Mark -> 40
Davis -> 50
James -> 70
'''

