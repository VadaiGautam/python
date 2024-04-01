# The writelines() method in Python is used to write a list of strings to a file. This method does not add newline characters{means \n dena padega newline me automatically  nhi jayega list items} between the list items automatically, so one must add them manually if needed. The writelines() method is more efficient than using a write() method in a loop.

f = open("file3.txt",'w')      # make new file automatically

lines =['line1\n','line2\n','line3\n']             # list form 

f.writelines(lines)     # f variable ke andar jo file open hui he uss file me ye list items ko add krna he 

print(f)

f.close()