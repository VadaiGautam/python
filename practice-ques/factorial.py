#  it can be call itself 
#  it can be use when - 


#  factorial program using recursively

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
    

n = int(input("enter the number"))
print(fac(n))
