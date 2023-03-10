list_of_words = [i for i in input().split()]


with open(r'C:\Users\elnur\OneDrive\Документы\PP II\Lab 6\Files\text.txt', 'w') as f:
    f.write('\n'.join(list_of_words))