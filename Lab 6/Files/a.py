import os
path=r'C:\Users\elnur\OneDrive\Документы\PP II\Lab 6'
files=os.listdir(path)
files = [filenames for filenames in files if os.path.isfile(path+'/'+filenames)]
direc = os.listdir(path)
direc = [dirname for dirname in files if os.path.isdir(path+'/'+dirname)]
print('List of directories:\n',direc)

print('List of files:\n',files)

print('List of directories and files:\n',os.listdir(path))