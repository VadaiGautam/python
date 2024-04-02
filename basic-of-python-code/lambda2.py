import math


def trible(fx , value):
    return fx(value)


#  function ke andar ek or function ko call 

print("Square root of 4 is : ",trible(math.sqrt,4))

                                # OR  

# square the number by function into function call

def trible(fx , value):
    return fx(value)


#  function ke andar ek or function ko call 

print("Square of 2 is : ",trible(lambda x: x*x,2))

