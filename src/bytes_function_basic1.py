'''
Python Bytes Function (Basic 1)

Example: Bytes Function Examples
'''
string = "Giannis Antetokounmpo"


# Encoded String
encoded = bytes(string, 'utf-8')


# Display
print(f"{string} -> {encoded}")

'''
Output:
Giannis Antetokounmpo -> b'Giannis Antetokounmpo'
'''

