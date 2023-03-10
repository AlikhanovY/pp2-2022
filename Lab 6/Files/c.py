import os

path = r'C:\Users\elnur\OneDrive\Документы\PP II\Lab 4'

test_existence = os.access(path, os.F_OK)
if test_existence:
    print(os.listdir(path))
else:
    print('given path not exists')