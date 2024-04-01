f = open('file2.txt','r')

i =0

while True:
    i=i+1

    line = f.readline()

    # Whenever there is a need to break bigger strings or a line into several small strings, you need to use the split() function in Python.

    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])

    print(f"Marks of {i} Student in Maths is : {m1}")
    print(f"Marks of {i} Student in Sci : {m2}")
    print(f"Marks of {i} Student in Computer : {m3}")
    print(' ')


