def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        print("not divisible")


print(sub(3,2))
print(add(3,2))
print(mul(3,2))
print(div(4,2))
print(div(3,0))

