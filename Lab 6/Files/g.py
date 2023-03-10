import os

with open(r"C:\Users\elnur\OneDrive\Документы\PP II\Lab 6\Files\text.txt") as f:
    data = f.read()

print(data)

with open(r'C:\Users\elnur\OneDrive\Документы\PP II\Lab 6\Files\text1.txt', 'w') as f2:
    f2.write(data)