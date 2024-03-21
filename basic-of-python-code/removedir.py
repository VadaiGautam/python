import os

import os.path

import shutil

shutil.rmtree('files')    # files - it is directory in this 2 txt file can exists. by the help or shutil we can remove dir. 

# os.remove('docs.txt')

a = os.listdir('.')
   
print(a)