# Write a Python program to multiply all the items in a list.

lisst =[]

n=int(input("no ."))
for i in range(0,n):
    liss=int(input("enter the list items : "))
    lisst.append(liss)
mul =1
for i in lisst:
    mul = mul * i

print(f"multiplication is {mul}")
