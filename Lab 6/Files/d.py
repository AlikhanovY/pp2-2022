path = r'C:\Users\elnur\OneDrive\Документы\PP II\Lab 6\Files\text.txt'
count = 0
with open(path, 'r') as file:
    for line in file:
        count+=1

print(f'The number of lines is: {count}')