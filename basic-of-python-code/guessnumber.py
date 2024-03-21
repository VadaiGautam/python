import random

target_num = random.randint(1,10)  # it can generate random number 

guess_num = 0
loopcount =0
print("enter the number between 1 to 10 ")
while target_num!=guess_num:
    guess_num=int(input("enter the number"))
    loopcount=loopcount+1


print("number found")

print("how many times you have worng",loopcount)

