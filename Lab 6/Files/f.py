import os, string

os.chdir(r'C:\Users\elnur\OneDrive\Рабочий стол\PP 2 files' )

alphabet = string.ascii_uppercase

for letter in alphabet:
    with open(letter+'.txt', 'w') as f:
        f.write(letter)