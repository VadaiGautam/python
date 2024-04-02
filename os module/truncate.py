with open('file5.txt','w') as f:

 f.write("this is a txt file")

 f.truncate(5)

f= open('file5.txt','r')

file = f.read()

print(file)
