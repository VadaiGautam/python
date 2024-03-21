number = int(input("enter five digit number"))



for i in range(5):
    a=int(number%10)
    number=int(number//10)
    print( a , end="" )