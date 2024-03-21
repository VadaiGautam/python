number = int(input("enter number"))

count =0

while number!=0:
    number = number //10
    count =count+1
    

print(f"it is {count} digit number")