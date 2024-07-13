import os

f = open("write.txt",'w')
l=["i am a fesher ","i am finding job \n"]

f.writelines(l)

''' writelines doesn't add newline char b/w string ,   so we use loop for newline'''


f =open("write.txt",'a')

lines =["i am a fesher ","i am finding job"]

for i in lines:
    f.write(i+"\n")
    



