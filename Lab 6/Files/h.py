import os

path=r"C:\Users\elnur\OneDrive\Документы\PP 2\Lab 1\Python Casting\1.py"
if os.access(path,os.F_OK):
    os.remove(path)
    print("file deleted")
else:
    print("file doesnt exist")