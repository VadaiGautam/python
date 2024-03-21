file = open('vadai.txt','a')           # append 'a' means ...adding new content at the last line .

file.write("\n my age is 21 years old  and my birth date is 25 july 2003\n")

file = open('vadai.txt','r')


content = file.read()

print(content)

file.close()