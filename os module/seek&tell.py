f = open("file4.txt",'r')

f.seek(10)

print(f.tell())     # ye hame batayega kha tak seek hua he ..... kitne aage se 

line = f.read()

print(line)