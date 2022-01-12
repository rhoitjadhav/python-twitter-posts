import os

path = "/home/rohit/Test"
for dirpath, dirs, files in os.walk(path):
    print(dirpath)
    print(dirs)
    print(files)
