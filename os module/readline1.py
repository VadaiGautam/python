f= open('file.txt','r')

# file = f.read()       # READ ALL LINES

# print(file)

# file2 = f.readlines()     # read all lines in the form of list 
# print(file2)

# file3 = f.readline()         # read only first line  
# print(file3)
i=1

while True:
    
    line = f.readline()
    print(f"read {i} line")
    
    if not line:
        break
    print(line)
    i = i+1