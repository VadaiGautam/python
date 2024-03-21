def name(nem,age):
    print(f"my name is {nem} and i am {age} year old")


name('vadai',6)
name ('pooja', 21)


def addition(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
    

def div(x,y):
    if y != 0 :
        return x/y
    else:
        print("not divisibe by zero")


print(f"addition is = {addition(6,7)}")
print(f"sub is = {sub(6,7)}")
print(f"mul is = {mul(6,7)}")

print(f"div is = {div(6,0)}")

