import os

path = r'C:\Users\elnur\OneDrive\Документы\PP II\Lab 4'


test_existence = os.access(path, os.F_OK)
print("test_existence: ", test_existence)

test_readability = os.access(path, os.R_OK)
print("test_readability: ", test_readability)

test_writability = os.access(path, os.W_OK)
print('test_writability: ', test_writability)

test_executed = os.access(path, os.X_OK)
print('test_executed: ', test_executed)
