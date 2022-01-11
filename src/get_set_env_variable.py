import os

os.environ["MYENV"] = "TEST"  # Set
print(os.getenv("MYENV"))  # Get

