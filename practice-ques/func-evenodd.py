''' number is even or odd '''


def evennum(num):
    return num%2==0

num = int(input("enter the number"))

if evennum(num):
    print(f"{num} number is even ")
else:
    print(f"{num} number is odd")