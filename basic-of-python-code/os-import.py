import os

import os.path

os.mkdir('folder1')   #  we can create a folder on the current directory

a= os.listdir('.')    #show all the files or folder in the current working directory

print(a)

x = os.path.exists('vadai.txt')    # it tells that file exists or not
f = os.path.exists('folder1') 
print(x)
print(f)
 
os.rmdir('folder1')

lisst = os.listdir('.')
print(lisst)